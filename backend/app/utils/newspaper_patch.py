# In a new file like app/utils/newspaper_patch.py
import nltk
from newspaper import Article

# Store the original nlp method
original_nlp = Article.nlp

# Create a patched version that ensures punkt is downloaded
def patched_nlp(self):
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
    
    # Also try to handle punkt_tab specifically
    try:
        nltk.data.find('tokenizers/punkt_tab')
    except LookupError:
        # punkt_tab may not exist as a separate download
        import os
        import shutil
        
        # Get the path to punkt
        punkt_path = nltk.data.find('tokenizers/punkt')
        if punkt_path:
            # Create punkt_tab directory structure
            punkt_dir = os.path.dirname(punkt_path)
            tokenizers_dir = os.path.dirname(punkt_dir)
            punkt_tab_dir = os.path.join(tokenizers_dir, 'punkt_tab', 'english')
            os.makedirs(punkt_tab_dir, exist_ok=True)
            
            # Copy files from punkt to punkt_tab
            for item in os.listdir(punkt_dir):
                src = os.path.join(punkt_dir, item)
                dst = os.path.join(punkt_tab_dir, item)
                if os.path.isfile(src) and not os.path.exists(dst):
                    shutil.copy2(src, dst)
    
    # Call the original nlp method
    return original_nlp(self)

# Apply the patch
Article.nlp = patched_nlp