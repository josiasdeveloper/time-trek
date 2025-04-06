from src.clients.http_async_client import HttpAsyncClient
from src.config import settings
from src.data.api_ninja import HistoricalEvents


class ApiNinjaAsyncClient:
    def __init__(self, api_key: str):
        self.http_client = HttpAsyncClient(
            base_url="https://api.api-ninjas.com/v1",
            headers={"X-Api-Key": api_key},
        )

    
    
    async def get_historical_data(self, month: int, year: int) -> HistoricalEvents:
        path = f"/historicalevents?year={year}&month={month}"
        response = await self.http_client.get(path)
        json_data = await response.json()
        
        # Extract only the events from the response
        events = [
            fact_data["event"]
            for fact_data in json_data
            if all(key in fact_data for key in ["year", "month", "day", "event"])
        ]
        
        return HistoricalEvents(year=year, month=month, events=events)
            

        


api_ninja_client = ApiNinjaAsyncClient(settings.api_ninja_api_key)