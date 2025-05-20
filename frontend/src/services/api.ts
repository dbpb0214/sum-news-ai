import { ErrorResponse, SummaryRequest, SummaryResult } from "../types";

const API_BASE_URL = 'http://localhost:8000/api';

export const summarizeArticle = async (request: SummaryRequest): Promise<SummaryResult> => {
    try {
        const response = await fetch(`${API_BASE_URL}/summarize_article`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(request),
        });
        if (!response.ok) {
            const errorData = await response.json() as ErrorResponse;
            throw new Error(errorData.message || "Failed to summarize article")
        }
        return await response.json() as SummaryResult
    } catch (error) {
        console.error('Error summarizing article: ', error)
        throw error;
    }
}