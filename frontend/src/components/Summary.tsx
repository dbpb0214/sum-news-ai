import { SummaryResult } from "@/types";

interface SummaryProps {
    summary: SummaryResult | null;
}

const Summary: React.FC<SummaryProps> = ({ summary }) => {
    if (!summary) return null;

    const formatDate = (timestamp: number): string => {
        return new Date(timestamp).toLocaleString();
    }

    const copyToClipboard = () => {
        const text = `${summary.title}\n\n${summary.openaiSummary}\n\nKeyPoints:\n${summary.keyPoints.map(point => `- ${point}`).join('\n')}`;
        navigator.clipboard.writeText(text).then(() => alert('Summary copied to clipboard!')).catch(() => alert('Failed to copy summary'))
    }

    return (
        <div className="summary-container">
            <h2>{summary.title}</h2>
            <div className="meta-info">
                <span>Reading time: {summary.readingTime} min</span> | 
                <span>Summarized on: {formatDate(summary.timestamp)}</span>
            </div>
            <div className="summary-text">
                <h3>Regular Summary</h3>
                <p>{summary.parserSummary ? summary.parserSummary : "No summary available from parser" }</p>
            </div>
            <div className="summary-text">
                <h3>OpenAI Summary</h3>
                <p>{summary.openaiSummary ? summary.openaiSummary : "No summary available from OpenAI" }</p>
            </div>
            <div className="key-points">
                <h3>Key Points</h3>
                <ul>
                    {summary.keyPoints.map((point, index) => (
                        <li key={index}>{point}</li>
                    ))}
                </ul>
            </div>
            <div className="original-link">
                <a href={summary.originalUrl} target="_blank" rel="noopener noreferrer">
                    Read Original Article
                </a>
            </div>
            <button onClick={copyToClipboard} className="copy-button">
                Copy Summary
            </button>
        </div>
    )
}
export default Summary