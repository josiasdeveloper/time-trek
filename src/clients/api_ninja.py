from http_async_client import HttpAsyncClient


class ApiNinjaAsyncClient:
    def __init__(self, api_key: str):
        self.http_client = HttpAsyncClient(
            base_url="https://api.api-ninjas.com/v1",
            headers={"X-Api-Key": api_key},
        )

    async def get_historical_data(self, month: int, year: int):
        path = f"/historicalevents?year={year}&month={month}"
        response = await self.http_client.get(path)
        return await response.json()
