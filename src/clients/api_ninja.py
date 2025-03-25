from src.clients.http_async_client import HttpAsyncClient
from src.config import settings
from src.data.api_ninja import HistoricalFact


class ApiNinjaAsyncClient:
    def __init__(self, api_key: str):
        self.http_client = HttpAsyncClient(
            base_url="https://api.api-ninjas.com/v1",
            headers={"X-Api-Key": api_key},
        )

    
    
    async def get_historical_data(self, month: int, year: int) -> list[HistoricalFact]:
        path = f"/historicalevents?year={year}&month={month}"
        response = await self.http_client.get(path)
        json_data = await response.json()
        
        # Filter for data with all required fields
        return [
            HistoricalFact(**fact_data)
            for fact_data in json_data
            if all(key in fact_data for key in ["year", "month", "day", "event"])
        ]
            

        


api_ninja_client = ApiNinjaAsyncClient(settings.api_ninja_api_key)