import { SummaryResult } from "@/types";

interface HistoryProps {
    history: SummaryResult[]
    onSelect: (summary: SummaryResult) => void;
    onClear: () => void;
}

const History: React.FC<HistoryProps> = ({ history, onSelect, onClear }) => {
    if (history.length === 0) {
        return (
            <div className="history-container empty">
                <h3>No History</h3>
                <p>Summarized articles will appear here</p>
            </div>
        )
    }

    const formatDate = (timestamp: number): string => {
        return new Date(timestamp).toLocaleDateString();
    }

    return (
        <div className="history-container">
            <div className="history-header">
                <h3>Recent Summaries</h3>
                <button onClick={onClear} className="clear-button">Clear All</button>
            </div>
            <ul className="history-list">
                {history.map((item, index) => (
                    <li key={index} onClick={() => onSelect(item)} className="history-item">
                        <div className="history-title">{item.title}</div>
                        <div className="history-meta">
                            <span>{new URL(item.originalUrl).hostname}</span>
                            <span>{formatDate(item.timestamp)}</span>
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    )
}

export default History;