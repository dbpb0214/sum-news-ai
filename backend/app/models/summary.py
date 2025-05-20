from datetime import datetime
from typing import List
from pydantic import BaseModel, Field, HttpUrl


class SummaryRequest(BaseModel):
    url: HttpUrl = Field(..., description="URL of the news article to summarize")

class SummaryResponse(BaseModel):
    originalUrl: str
    title: str
    parserSummary: str
    openaiSummary: str
    keyPoints: List[str]
    readingTime: int
    timestamp: int = Field(default_factory=lambda: int(datetime.now().timestamp() * 1000))