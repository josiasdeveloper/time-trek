from datetime import UTC, datetime
from typing import List, Optional

from pydantic import BaseModel, Field

from src.config import settings


class HistoricalFactDetail(BaseModel):
    title: str
    content: str
    attachments: Optional[List[str]] = None


class HistoricalFactResponse(BaseModel):
    month: int
    year: int
    day: int
    facts: List[HistoricalFactDetail]


class HistoricalFactsAPIResponse(BaseModel):
    date: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    total_facts: int
    historical_facts: List[HistoricalFactDetail]
    metadata: dict = Field(default_factory=lambda: {
        "source": "API Ninjas",
        "enhanced_by": "GPT-3.5",
        "batch_size": settings.batch_size
    })
