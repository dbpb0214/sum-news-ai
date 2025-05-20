import { useState } from "react";
import URLForm from './components/URLForm';
import { summarizeArticle } from "./services/api";
import { SummaryResult } from "./types";
import { clearHistory, getHistory, saveToHistory } from "./utils/storage";
import Summary from "./components/Summary";
import History from './components/History';


const App: React.FC = () => {
    const [isLoading, setIsLoading] = useState<boolean>(false);
    const [error, setError] = useState<string>('');
    const [currentSummary, setCurrentSummary] = useState<SummaryResult | null>(null);
    const [history, setHistory] = useState<SummaryResult[]>([])

    const handleSubmit = async (url: string) => {
        setIsLoading(true)
        setError('')
        try {
            const result = await summarizeArticle({ url })
            setCurrentSummary(result)
            saveToHistory(result);
            setHistory(getHistory())
        } catch (err) {
            setError(err instanceof Error ? err.message : 'Failed to summarize article')
            setCurrentSummary(null)
        } finally {
            setIsLoading(false)
        }
    }

    const handleSelectFromHistory = (summary: SummaryResult) => {
        setCurrentSummary(summary);
    }

    const handleClearHistory = () => {
        clearHistory()
        setHistory([])
    }

    return (
        <div className="app-container">
            <header className="app-header">
                <h1>News Article Summarizer</h1>
                <p>Enter a news article URL to get a concise summary</p>
            </header>

            <main>
                <URLForm onSubmit={handleSubmit} isLoading={isLoading}/>
                {error && <div className="error-container">{error}</div>}

                <div className="content-container">
                    <div className="summary-section">
                        {isLoading ? (
                            <div className="loading">Summarizing article</div>
                        ) : (
                            <Summary summary={currentSummary}/>
                        )}
                    </div>
                    <aside className="history-section">
                        <History
                            history={history}
                            onSelect={handleSelectFromHistory}
                            onClear={handleClearHistory}
                        />
                    </aside>
                </div>
            </main>
            <footer>
                <p>Powered by OpenAI + Newspaper3k + spaCy</p>
            </footer>
        </div>
    )
}

export default App;