from pydantic import BaseModel


class HistoricalFact(BaseModel):
    year: int
    month: int
    day: int
    event: str


