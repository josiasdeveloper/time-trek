from logging import getLogger

from openai import AsyncOpenAI

from src.config import settings
from src.data.api_ninja import HistoricalEvents
from src.data.open_ai import HistoricalFactResponse

logger = getLogger(__name__)

class OpenAIAsyncClient:
    def __init__(self):
        self.client = AsyncOpenAI(api_key=settings.openai_api_key)
        
    async def get_historical_fact(
        self, 
        historical_events: HistoricalEvents,
        page_size: int = settings.batch_size
    ) -> list[HistoricalFactResponse]:
        logger.info(f"Processing historical events for {historical_events.year}-{historical_events.month}-{historical_events.day}")
        paginated_events = historical_events.paginate_events(page_size)
        logger.debug(f"Split events into {len(paginated_events)} batches of size {page_size}")
        responses = []
        
        for i, event_batch in enumerate(paginated_events, 1):
            logger.debug(f"Processing batch {i} of {len(paginated_events)}")
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
                 "day": {day},
                 "facts": [
                   {{
                     "title": "The original historical fact",
                     "content": "Detailed explanation in Brazilian Portuguese - If there are any URLs, they will be in the attachments field. Avoid them here",
                     "attachments": null  // Use real URLs only, otherwise null. I'm using json to parse the response so this need to be a json array inside []
                   }}
                 ]
               }}

            Time period: Month: {month}, Year: {year}, Day: {day}
            Historical facts to analyze: {historical_facts}

            Important:
            - All explanations in 'content' must be in Brazilian Portuguese
            - All titles must be in Brazilian Portuguese, ensure to translate everything
            - Keep the content field focused on the explanation only, no URLs or references
            - NEVER use example.com or placeholder URLs
            - Only include URLs you are 100% certain exist and are relevant
            - If you don't have a verified source URL, use null for attachments
            - Ensure JSON format is exactly as specified
            """.format(month=historical_events.month, year=historical_events.year, day=historical_events.day, historical_facts=event_batch)
            
            response = await self._get_response(message)
            try:
                parsed_response : HistoricalFactResponse = HistoricalFactResponse.model_validate_json(response)
                responses.append(parsed_response)
                logger.debug(f"Successfully processed batch {i}")
            except Exception as error:
                logger.error(f"Failed to parse GPT response in batch {i}: {str(error)}")
                responses.append(response)
        
        logger.info(f"Completed processing all {len(responses)} response batches")
        return responses

    async def _get_response(self, message: str) -> str:
        logger.debug("Sending request to OpenAI API")
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4o-search-preview-2025-03-11",
                messages=[
                    {"role": "user", "content": message}
                ]
            )
            content = response.choices[0].message.content or ""
            content = content.replace("```json", "").replace("```", "").strip()
            logger.debug("Successfully received and cleaned OpenAI response")
            return content
        except Exception as e:
            logger.error(f"Error getting OpenAI response: {str(e)}")
            raise
    
    
openai_client = OpenAIAsyncClient() # export singleton instance