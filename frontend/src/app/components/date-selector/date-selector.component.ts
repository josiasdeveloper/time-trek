import { Component, EventEmitter, Output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { MatDatepickerModule } from '@angular/material/datepicker';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatNativeDateModule } from '@angular/material/core';
import { trigger, transition, style, animate } from '@angular/animations';

@Component({
  selector: 'app-date-selector',
  standalone: true,
  imports: [
    CommonModule, 
    ReactiveFormsModule,
    MatButtonModule,
    MatDatepickerModule,
    MatFormFieldModule,
    MatInputModule,
    MatNativeDateModule
  ],
  templateUrl: './date-selector.component.html',
  styleUrl: './date-selector.component.css',
  animations: [
    trigger('fadeIn', [
      transition(':enter', [
        style({ opacity: 0, transform: 'translateY(20px)' }),
        animate('0.5s ease-out', style({ opacity: 1, transform: 'translateY(0)' }))
      ])
    ])
  ]
})
export class DateSelectorComponent {
  @Output() dateSelected = new EventEmitter<{day: number, month: number, year: number}>();
  dateForm: FormGroup;
  maxDate = new Date();
  minDate = new Date(1900, 0, 1);
  
  constructor(private fb: FormBuilder) {
    this.dateForm = this.fb.group({
      selectedDate: [null, [Validators.required]]
    });
  }

  onSubmit() {
    if (this.dateForm.valid) {
      const date = this.dateForm.value.selectedDate as Date;
      this.dateSelected.emit({
        day: date.getDate(),
        month: date.getMonth() + 1, // JavaScript months are 0-indexed
        year: date.getFullYear()
      });
    }
  }
}
