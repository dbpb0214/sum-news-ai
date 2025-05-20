export interface SummaryResult {
    originalUrl: string;
    title: string;
    parserSummary: string;
    openaiSummary: string;
    keyPoints: string[];
    readingTime: number;
    timestamp: number;
}

export interface SummaryRequest {
    url: string;
}

export interface ErrorResponse {
    error: string;
    message: string;
}