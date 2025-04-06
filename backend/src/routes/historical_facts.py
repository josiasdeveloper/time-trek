from datetime import UTC, datetime
from typing import List

from fastapi import APIRouter

from src.clients.api_ninja import api_ninja_client
from src.clients.open_ai import openai_client
from src.data.open_ai import (
    HistoricalFactDetail,
    HistoricalFactResponse,
    HistoricalFactsAPIResponse,
)

router = APIRouter()

@router.get("/historical-facts", response_model=HistoricalFactsAPIResponse)
async def get_historical_facts(month: int, year: int):
    historical_facts = await api_ninja_client.get_historical_data(month, year)
    chatgpt_responses = await openai_client.get_historical_fact(month, year, historical_facts)
    
    # Flatten all facts from all responses into a single list
    all_facts: List[HistoricalFactDetail] = []
    for response in chatgpt_responses:
        if isinstance(response, HistoricalFactResponse):
            all_facts.extend(response.facts)
    
    return HistoricalFactsAPIResponse(
        date=f"{year}-{month:02d}",
        timestamp=datetime.now(UTC),
        total_facts=len(all_facts),
        historical_facts=all_facts
    )