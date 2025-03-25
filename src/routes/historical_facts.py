

from fastapi import APIRouter

from src.clients.open_ai import openai_client

router = APIRouter()


@router.get("/historical-facts")
async def get_historical_facts(date: str):
    chatgpt_response = await openai_client.get_response("Hello World")

    return {
        "date": date,
        "historicalFacts": [
            {
                "fact": "Teste simples com ChatGPT",
                "aiEnhancedExplanation": chatgpt_response
            }
        ]
    }
    
    