import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { DateSelectorComponent } from './components/date-selector/date-selector.component';
import { HistoricalFactsComponent } from './components/historical-facts/historical-facts.component';
import { trigger, transition, style, animate } from '@angular/animations';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, DateSelectorComponent, HistoricalFactsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
  animations: [
    trigger('fadeIn', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(20px)' }),
        animate('0.5s ease-out', style({ opacity: 1, transform: 'translateY(0)' }))
      ])
    ])
  ]
})
export class AppComponent {
  selectedDate: { day: number; month: number; year: number } | null = null;
  showingEvents = false;

  onDateSelected(date: { day: number; month: number; year: number }) {
    // If we already have a date and are just navigating back to select a new one,
    // clear it first so the component will properly re-fetch when we set it again
    if (this.selectedDate) {
      this.selectedDate = null;
      // Small delay to ensure the component registers the change
      setTimeout(() => {
        this.selectedDate = date;
        this.showingEvents = true;
      }, 50);
    } else {
      this.selectedDate = date;
      this.showingEvents = true;
    }
  }
  
  goBackToDateSelection() {
    this.showingEvents = false;
  }
}
