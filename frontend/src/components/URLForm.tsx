import React, { useState } from "react";

interface URLFormProps {
    onSubmit: (url: string) => void;
    isLoading: boolean;
}

const URLForm: React.FC<URLFormProps> = ({ onSubmit, isLoading }) => {
    const [url, setUrl] = useState<string>('');
    const [error, setError] = useState<string>('');

    const validateUrl = (value: string): boolean => {
        try {
            new URL(value)
            return true;
        } catch {
            return false;
        }
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault()
        if (!url.trim()) {
            setError('Please enter URL');
            return
        }

        if (!validateUrl(url)) {
            setError('Please enter a valid URL');
            return
        }

        setError('')
        onSubmit(url)
    }
    return (
        <form onSubmit={handleSubmit} className="url-form">
            <div className="input-container">
                <input
                    type="text"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                    placeholder="Enter news article URL..."
                    disabled={isLoading}
                    className="url-input"
                />
                <button type="submit" disabled={isLoading} className="submit-button">
                    { isLoading ? 'Summarizing...': 'Summarize' }
                </button>
            </div>
            {error && <p className="error-message">{error}</p>}
        </form>
    );
};

export default URLForm