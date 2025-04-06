from openai import AsyncOpenAI

from src.config import settings
from src.data.api_ninja import HistoricalEvents
from src.data.open_ai import HistoricalFactResponse


class OpenAIAsyncClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        
    async def get_historical_fact(
        self, 
        month: int, 
        year: int, 
        historical_events: HistoricalEvents, 
        page_size: int = settings.batch_size
    ) -> list[HistoricalFactResponse]:
        paginated_events = historical_events.paginate_events(page_size)
        responses = []
        
        for event_batch in paginated_events:
            message = """
            You are a knowledgeable historical research assistant. Analyze these historical events and provide detailed context.

            Instructions:
            1. Create a comprehensive explanation for each historical fact
            2. Include context about the time period and historical impact
            3. For sources, ONLY include real, verifiable URLs from reputable sources like:
               - Do not use example.com or placeholder URLs
               - Those URLs are very important to the user, always try to find them
               - If you're not 100%% certain about a URL's authenticity, use null instead
            4. Try to look like a news reporter, with a tone of curiosity and excitement
            5. Do not use too much technical terms, keep it simple and easy to understand
            6. Format your response in JSON with this structure:
               {{
                 "month": {month},
                 "year": {year},
                 "day": 1,
                 "facts": [
                   {{
                     "title": "The original historical fact",
                     "content": "Detailed explanation in Brazilian Portuguese - If there are any URLs, they will be in the attachments field. Avoid them here",
                     "attachments": null  // Use real URLs only, otherwise null
                   }}
                 ]
               }}

            Time period: Month: {month}, Year: {year}
            Historical facts to analyze: {historical_facts}

            Important:
            - All explanations in 'content' must be in Brazilian Portuguese
            - All titles must be in Brazilian Portuguese, ensure to translate everything
            - Keep the content field focused on the explanation only, no URLs or references
            - NEVER use example.com or placeholder URLs
            - Only include URLs you are 100% certain exist and are relevant
            - If you don't have a verified source URL, use null for attachments
            - Ensure JSON format is exactly as specified
            """.format(month=month, year=year, historical_facts=event_batch)
            
            response = await self._get_response(message)
            try:
                parsed_response = HistoricalFactResponse.model_validate_json(response)
                responses.append(parsed_response)
            except Exception as e:
                print(f"Failed to parse GPT response: {e}")
                responses.append(response)
        
        return responses

    async def _get_response(self, message: str) -> str:
        response = await self.client.chat.completions.create(
            model="gpt-4o-search-preview",
            messages=[
                {"role": "user", "content": message}
            ]
        )
        # Clean up the response by removing markdown code blocks
        content = response.choices[0].message.content or ""
        content = content.replace("```json", "").replace("```", "").strip()
        print(response)
        return content
    
    
openai_client = OpenAIAsyncClient() # export singleton instance