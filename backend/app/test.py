# test_newspaper.py
import os
import sys
import logging
import nltk
import shutil

# Setup logging to see what's happening
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 1. Print all NLTK data paths
logger.debug("NLTK data paths: %s", nltk.data.path)

# 2. Download punkt explicitly
nltk.download('punkt')

# 3. Check if punkt is now available
try:
    punkt_path = nltk.data.find('tokenizers/punkt')
    logger.debug("Found punkt at: %s", punkt_path)
except LookupError:
    logger.error("Could not find punkt after downloading")

# 4. Now try importing newspaper and see what happens
from newspaper import Article

# 5. Create a simple article
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
article = Article(url)

# 6. Try downloading and parsing
try:
    article.download()
    article.parse()
    logger.debug("Article downloaded and parsed successfully")
except Exception as e:
    logger.error("Error downloading/parsing article: %s", e)

# 7. Now try NLP, which we expect to fail with punkt_tab error
try:
    # Add a hook to track NLTK resource loading
    original_find = nltk.data.find
    def debug_find(resource_name, *args, **kwargs):
        logger.debug("NLTK looking for resource: %s", resource_name)
        return original_find(resource_name, *args, **kwargs)
    
    nltk.data.find = debug_find
    
    # Try running nlp
    article.nlp()
    logger.debug("Article NLP succeeded unexpectedly")
except Exception as e:
    logger.error("Error during NLP: %s", e)

# 8. Specifically look for punkt_tab
try:
    punkt_tab_path = nltk.data.find('tokenizers/punkt_tab')
    logger.debug("Found punkt_tab at: %s", punkt_tab_path)
except LookupError:
    logger.error("Could not find punkt_tab as expected")