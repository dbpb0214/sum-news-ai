import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class OpenAIService:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        
    def summarize_text(self, text: str, title: str) -> dict:
        """Use OpenAI API to summarize text."""
        try:
            client = OpenAI()
            completion = client.chat.completions.create(
                model="gpt-4.1",
                messages=[
                    {
                        "role": "user",
                        "content": f"""
                            Take the news article text given and generate a concise summary of about 90 words and outline 3 short key points on the text (use '-' for list items, not numbers or letters). 
                            Separate the summary and key points with the word "Key Points": {text}"""
                    }
                ]
            )
            # print("GPT RESP: ", completion.choices[0].message.content)
            gpt_response = completion.choices[0].message.content.split("Key Points:")
            gpt_summary = gpt_response[0]
            gpt_key_points = gpt_response[1]

            # print("gpt_summary: ", gpt_summary)
            print("gpt_key_points: ", gpt_key_points.split("-"))

            key_points = []
            for kp in gpt_key_points.split("-"):
                kp_stripped = kp.strip()
                if len(kp_stripped) > 10:
                    key_points.append(kp_stripped)

            return {
                "summary": gpt_summary,
                "key_points": key_points
            }
        except Exception as e:
            raise Exception(f"OpenAI API error: {str(e)}")
        