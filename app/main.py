from fastapi import FastAPI
from openai import AsyncOpenAI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
client = AsyncOpenAI(api_key=settings.openai_api_key)

app = FastAPI()

@app.get("/api/historical-facts")
async def get_historical_facts(date: str):
    response = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Hello World"}
        ]
    )
    chatgpt_response = response.choices[0].message.content

    return {
        "date": date,
        "historicalFacts": [
            {
                "fact": "Teste simples com ChatGPT",
                "aiEnhancedExplanation": chatgpt_response
            }
        ]
    }