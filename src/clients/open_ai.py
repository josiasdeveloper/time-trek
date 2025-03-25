from openai import AsyncOpenAI

from src.config import settings
from src.data.api_ninja import HistoricalFact


class OpenAIAsyncClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        
        
    async def get_historical_fact(self, month: int, year: int, facts: list[HistoricalFact]) -> str:
        message = """
        Você é um assistente prestativo que pode responder perguntas sobre a história do mundo.
        Você receberá um fato histórico, um mês e um ano, e deve procurar informações, noticias, curiosidades, e deve fazer um texto sobre o fato histórico para o mês e ano fornecido.
        as infos virão a seguir : Mês : {month} e Ano : {year}, Fato histórico : {historical_fact}
        """.format(month=month, year=year, historical_fact=facts)
        return await self._get_response(message)

    async def _get_response(self, message: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        return response.choices[0].message.content or ""
    
    
openai_client = OpenAIAsyncClient() # export singleton instance