import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HistoricalFactsResponse } from '../models/historical-fact.model';

@Injectable({
  providedIn: 'root'
})
export class HistoricalFactsService {
  private apiUrl = 'http://localhost:9000/api/historical-facts';

  constructor(private http: HttpClient) {}

  getHistoricalFacts(day: number, month: number, year: number): Observable<HistoricalFactsResponse> {
    return this.http.get<HistoricalFactsResponse>(`${this.apiUrl}?day=${day}&month=${month}&year=${year}`);
  }
}
