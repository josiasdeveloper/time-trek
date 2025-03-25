from fastapi import APIRouter

from src.clients.api_ninja import api_ninja_client
from src.clients.open_ai import openai_client

router = APIRouter()


@router.get("/historical-facts")
async def get_historical_facts(month: int, year: int):
    historical_facts = await api_ninja_client.get_historical_data(month, year)
    
    chatgpt_response = await openai_client.get_historical_fact(month, year, historical_facts)
    
    return {
        "date": f"{year}-{month:02d}",
        "historicalFacts": [
            {
                "facts": historical_facts,
                "aiEnhancedExplanation": chatgpt_response
            }
        ]
    }
    
    