# ai_processing/ai_reviewer.py

import together
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

# Initialize Together AI client
client = together.Together(api_key=api_key)

def ai_review(text):
    print("AI Reviewer module loaded - Together AI in use.")

    output = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # Free Together AI model
        messages=[
            {"role": "system", "content": "You are an expert book content reviewer. Improve clarity, grammar, and flow of this content."},
            {"role": "user", "content": f"Review and improve this spun content:\n\n{text}"}
        ],
        max_tokens=500,
        temperature=0.7
    )

    reviewed_text = output.choices[0].message.content
    return reviewed_text
