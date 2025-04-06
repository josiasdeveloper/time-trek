from typing import List

from pydantic import BaseModel


class HistoricalEvents(BaseModel):
    year: int
    month: int
    events: List[str]
    def paginate_events(self, page_size: int) -> List[List[str]]:
        """Split events into pages of specified size"""
        return [self.events[i:i + page_size] for i in range(0, len(self.events), page_size)]





