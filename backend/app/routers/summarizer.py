from app.utils.newspaper_patch import *

from fastapi import APIRouter, HTTPException

from app.models.summary import SummaryRequest, SummaryResponse
from app.services.openai_service import OpenAIService
from app.services.scraper_service import ScraperService


router = APIRouter()
scrapper_service = ScraperService()
openai_service = OpenAIService()

@router.post("/summarize_article", response_model=SummaryResponse)
async def summarize_article(request: SummaryRequest):
    try:
        article_data = scrapper_service.extract_article(str(request.url))
        print("article_data: ", article_data)
        openai_response = openai_service.summarize_text(
            text=article_data['text'],
            title=article_data['title']
        )
        print("openai_response: ", openai_response)
        return SummaryResponse(
            originalUrl=str(request.url),
            title=article_data['title'],
            parserSummary=article_data['summary'],
            openaiSummary=openai_response['summary'],
            keyPoints=openai_response['key_points'],
            readingTime=article_data['estimated_reading_time']
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))