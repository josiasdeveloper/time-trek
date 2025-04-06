export interface HistoricalFact {
  title: string;
  content: string;
  attachments: string[] | null;
}

export interface HistoricalFactsResponse {
  date: string;
  timestamp: string;
  total_facts: number;
  historical_facts: HistoricalFact[];
  metadata: {
    source: string;
    enhanced_by: string;
    batch_size: number;
  };
}
