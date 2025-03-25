from openai import AsyncOpenAI
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
client = AsyncOpenAI(api_key=settings.openai_api_key)

class OpenAIAsyncClient:
    async def get_response(self, message: str) -> str:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content