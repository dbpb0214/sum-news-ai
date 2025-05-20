from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import summarizer

app = FastAPI(
    title="News Article Summarizer API",
    description="API for summarizing news articles using OpenAI and newspaper3k",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarizer.router, prefix="/api", tags=["summarizer"])

@app.get("/")
async def root():
    return {"message": "Welcome to the News Article Summarizer API"}

@app.get("/health")
async def health_check():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)