from openai import AsyncOpenAI

from src.config import settings


class OpenAIAsyncClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)

    async def get_response(self, message: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content or ""
    
    
openai_client = OpenAIAsyncClient() # export singleton instance