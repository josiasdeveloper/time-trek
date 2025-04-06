import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { CommonModule } from '@angular/common';
import {  HistoricalFactsResponse } from '../../models/historical-fact.model';
import { HistoricalFactsService } from '../../services/historical-facts.service';

@Component({
  selector: 'app-historical-facts',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './historical-facts.component.html',
  styleUrl: './historical-facts.component.css'
})
export class HistoricalFactsComponent implements OnChanges {
  @Input() selectedDate: {day: number, month: number, year: number} | null = null;
  factsResponse: HistoricalFactsResponse | null = null;
  loading = false;
  error: string | null = null;

  constructor(private historicalFactsService: HistoricalFactsService) {}

  ngOnChanges(changes: SimpleChanges): void {
    if (changes['selectedDate'] && this.selectedDate) {
      this.fetchHistoricalFacts();
    }
  }

  fetchHistoricalFacts(): void {
    if (!this.selectedDate){
      return;
    }

    this.loading = true;
    this.error = null;

    this.historicalFactsService.getHistoricalFacts(
      this.selectedDate.day,
      this.selectedDate.month,
      this.selectedDate.year
    ).subscribe({
      next: (data) => {
        this.factsResponse = data;
        this.loading = false;
      },
      error: (err) => {
        console.error('Error fetching historical facts:', err);
        this.error = 'Failed to load historical facts. Please try again.';
        this.loading = false;
      }
    });
  }
}
