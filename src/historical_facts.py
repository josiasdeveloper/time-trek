

from fastapi import FastAPI

from src.clients.open_ai import OpenAIAsyncClient

app = FastAPI()
openai_client = OpenAIAsyncClient()

@app.get("/api/historical-facts")
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