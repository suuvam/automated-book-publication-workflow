import together
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("TOGETHER_API_KEY")

client = together.Together(api_key=api_key)

def ai_write(text):
    print("AI Writer module loaded - Together AI in use.")

    output = client.chat.completions.create(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",  # Free Together.AI model
        messages=[
            {"role": "system", "content": "You are a helpful book content spinner."},
            {"role": "user", "content": f"Spin this content for me:\n\n{text}"}
        ],
        max_tokens=500,
        temperature=0.7
    )

    spun_text = output.choices[0].message.content
    return spun_text
