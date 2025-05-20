import { SummaryResult } from "../types";

const STORAGE_KEY = 'news-summary-history';

export const saveToHistory = (summary: SummaryResult): void => {
    try {
        const existingHistory = getHistory();
        const isDuplicate = existingHistory.some(item => item.originalUrl === summary.originalUrl);

        if (!isDuplicate) {
            const updatedHistory = [summary, ...existingHistory].slice(0, 10) // Keep only latest 10 items
            localStorage.setItem(STORAGE_KEY, JSON.stringify(updatedHistory))
        }
    } catch (error) {
        console.error('Error saving to history: ', error)
    }
};

export const getHistory = (): SummaryResult[] => {
    try {
        const history = localStorage.getItem(STORAGE_KEY);
        return history ? JSON.parse(history) : [];
    } catch (error) {
        console.error('Error retrieving history: ', error);
        return [];
    }
}

export const clearHistory = (): void => {
    try {
        localStorage.removeItem(STORAGE_KEY);
    } catch (error) {
        console.error('Error clearing history: ', error)
    }
}
