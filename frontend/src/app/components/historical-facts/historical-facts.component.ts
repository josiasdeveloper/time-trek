import { Component, Input, OnInit, AfterViewInit, OnChanges, SimpleChanges, ViewChild, ElementRef, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { HistoricalFactsService } from '../../services/historical-facts.service';

interface HistoricalFact {
  title: string;
  content: string;
  attachments: string[];
}

interface FactsResponse {
  date: string;
  total_facts: number;
  historical_facts: HistoricalFact[];
  metadata: {
    source: string;
    enhanced_by: string;
  };
}

@Component({
  selector: 'app-historical-facts',
  standalone: true,
  imports: [CommonModule, MatIconModule],
  templateUrl: './historical-facts.component.html',
  styleUrl: './historical-facts.component.css'
})
export class HistoricalFactsComponent implements OnInit, AfterViewInit, OnChanges, OnDestroy {
  @Input() selectedDate: { day: number; month: number; year: number } | null = null;
  @ViewChild('carousel') carouselRef: ElementRef | undefined;
  @ViewChild('progressBar') progressBarRef: ElementRef | undefined;
  
  factsResponse: FactsResponse | null = null;
  loading = false;
  error: string | null = null;
  private scrollListener: (() => void) | null = null;
  
  constructor(private historicalFactsService: HistoricalFactsService) {}

  ngOnInit() {
    if (this.selectedDate) {
      this.fetchHistoricalFacts();
    }
  }
  
  ngOnChanges(changes: SimpleChanges) {
    // Check if selectedDate has changed
    if (changes['selectedDate'] && changes['selectedDate'].currentValue) {
      // Reset data and fetch new facts
      this.factsResponse = null;
      this.fetchHistoricalFacts();
    }
  }

  ngAfterViewInit() {
    setTimeout(() => {
      this.setupScrollListeners();
    }, 500);
  }

  ngOnDestroy() {
    this.removeScrollListeners();
  }

  fetchHistoricalFacts() {
    if (!this.selectedDate) return;

    this.loading = true;
    this.error = null;

    this.historicalFactsService.getHistoricalFacts(
      this.selectedDate.day,
      this.selectedDate.month,
      this.selectedDate.year
    ).subscribe({
      next: (data) => {
        this.factsResponse = data as unknown as FactsResponse;
        this.loading = false;
        
        // Setup scroll listeners after data is loaded
        setTimeout(() => {
          this.setupScrollListeners();
          // Scroll carousel to beginning when new data is loaded
          if (this.carouselRef?.nativeElement) {
            this.carouselRef.nativeElement.scrollLeft = 0;
          }
        }, 200);
      },
      error: (err) => {
        console.error('Error fetching historical facts:', err);
        this.error = 'Failed to fetch historical events. Please try again.';
        this.loading = false;
      }
    });
  }

  setupScrollListeners() {
    // Remove any existing listeners first
    this.removeScrollListeners();
    
    // Wait for ViewChild references to be available
    setTimeout(() => {
      if (!this.carouselRef || !this.progressBarRef) return;
      
      const carouselEl = this.carouselRef.nativeElement;
      const progressBarEl = this.progressBarRef.nativeElement;
      
      if (carouselEl && progressBarEl) {
        const updateScrollProgress = () => {
          const scrollLeft = carouselEl.scrollLeft;
          const scrollWidth = carouselEl.scrollWidth;
          const clientWidth = carouselEl.clientWidth;
          
          // Calculate scroll percentage with bounds checking
          const maxScroll = scrollWidth - clientWidth;
          const scrollPercent = maxScroll <= 0 ? 0 : (scrollLeft / maxScroll) * 100;
          
          // Update the progress bar width
          progressBarEl.style.width = `${scrollPercent}%`;
        };
        
        // Initial update
        updateScrollProgress();
        
        // Store the listener function for cleanup
        this.scrollListener = updateScrollProgress;
        
        // Add scroll event listener
        carouselEl.addEventListener('scroll', this.scrollListener);
        
        // Also update on window resize
        window.addEventListener('resize', this.scrollListener);
      }
    }, 100);
  }
  
  removeScrollListeners() {
    if (this.scrollListener) {
      if (this.carouselRef && this.carouselRef.nativeElement) {
        this.carouselRef.nativeElement.removeEventListener('scroll', this.scrollListener);
      }
      window.removeEventListener('resize', this.scrollListener);
      this.scrollListener = null;
    }
  }
  
  getDomainName(url: string): string {
    try {
      // Try to create URL object
      const urlObj = new URL(url);
      // Get hostname without www. prefix
      let domain = urlObj.hostname.replace(/^www\./, '');
      
      // Handle special cases
      if (domain.includes('wikipedia.org')) {
        return 'wikipedia.org';
      } else if (domain.includes('nytimes.com')) {
        return 'nytimes.com';
      } else if (domain.includes('bbc.co.uk')) {
        return 'bbc.co.uk';
      }
      
      return domain;
    } catch (e) {
      // If URL is invalid, extract domain using regex
      const match = url.match(/^(?:https?:\/\/)?(?:www\.)?([^\/]+)/i);
      return match ? match[1] : url;
    }
  }
}
