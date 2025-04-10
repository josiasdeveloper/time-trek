from logging import getLogger
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

logger = getLogger(__name__)

@router.get("/historical-facts", response_model=HistoricalFactsAPIResponse)
async def get_historical_facts(month: int, year: int, day: int):
    logger.info(f"Received request for historical facts: {year}-{month}-{day}")
    try:
        historical_facts = await api_ninja_client.get_historical_data(month, year, day)
        logger.info("Successfully retrieved historical data from API Ninja")
        
        chatgpt_responses = await openai_client.get_historical_fact(historical_facts)
        logger.info("Successfully processed facts through OpenAI")
        
        all_facts: List[HistoricalFactDetail] = []
        for response in chatgpt_responses:
            if isinstance(response, HistoricalFactResponse):
                all_facts.extend(response.facts)
        
        logger.info(f"Returning {len(all_facts)} processed historical facts")
        return HistoricalFactsAPIResponse(
            date=f"{year}-{month:02d}-{day:02d}",
            historical_facts=all_facts,
            total_facts=len(all_facts)
        )
    except Exception as e:
        logger.error(f"Error processing historical facts request: {str(e)}")
        raise