import time
import spacy

from newspaper import Article, Config

nlp = spacy.load("en_core_web_sm")

class ScraperService:
    def __init__(self):
        pass

    def extract_article(self, url: str) -> dict:
        """
        Extract article content using newspaper3k, summarize using spaCy and OpenAI
        """
        
        strip_url = url.strip()
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        config = Config()
        config.browser_user_agent = user_agent
        article = Article(url=strip_url, language='en', config=config)
        article.download()
        article.parse()

        title = article.title
        authors = article.authors
        published_date = article.publish_date
        text = article.text

        doc = nlp(text)
        sentences = [sent.text.strip() for sent in doc.sents]
        summary = ' '.join(sentences[:3])
        estimated_reading_time = self.calculate_reading_time(text)

        try:
            time.sleep(0.5)
            return {
                "title": title,
                "text": text,
                "authors": authors,
                "publish_date": published_date,
                "summary": summary,
                "estimated_reading_time": estimated_reading_time
            }
        except Exception as e:
            raise Exception(f"Failed to extract article: {str(e)}")
    
    def calculate_reading_time(self, text: str) -> int:
        """Calculate estimated reading time in minutes."""

        words = len(text.split())
        # Assumes avg reading speed is 200 words per minute
        reading_time = max(1, round(words / 200))
        return reading_time