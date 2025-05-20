# Summarize news articles w/ AI and NLP

A lightweight app to run locally to summarize the news for you.


![Sum News](https://github.com/dbpb0214/sum-news-ai/raw/main/sum-news-screenshot.png)

## Overview

Sum News is a web app that takes an article link and returns a summary from two different mechanisms: one from an NLP library(spaCy) and from OpenAI. We also use newspaper3k to extract text. This web app can also store up to 10 articles and they are each selectable.

## Features

- **Summary Comparison**: See how OpenAI summarizes vs spaCy
- **History**: Automatically save up to 10 articles summaries in memory
- **Reading Time**: Get an idea of how long it would take to read the entire article

## Installation

### Developer Installation
1. Clone the repository:
   ```
   git clone git@github.com:dbpb0214/sum-news-ai.git
   cd sum-news-ai
   ```

## Tech Stack

- **Frontend**: React + TypeScript
- **Storage**: In-memory (you stop the local server it's gone)
- **Backend**: Python w/ spaCy, OpenAI, and newspaper3k 

## Usage

1. Once you have cloned the project you can start up the backend and frontend
2. You will need to setup your openai_api key as well in the .env file. Go to OpenAI here: platform.openai.com for your API key
3. To start the frontend: cd frontend/ -> npm run start
4. To start the backend: cd backend/ -> uvicorn app.main:app --reload --port 8000

## Development

### Prerequisites
- Python
- React + TypeScript

## Privacy Policy

Sum News respects your privacy. By default, all data is stored locally in your browser or in memory in the app. We do not collect data. 

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Project Link: [https://github.com/dbpb0214/sum-news-ai](https://github.com/dbpb0214/sum-news-ai)

---

Made with ❤️ by [Desmond Beramendi]