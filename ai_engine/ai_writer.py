import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

def generate_content(chapter_text: str, prompt_template: str = None) -> str:
    if not prompt_template:
        prompt_template = (
            "Rewrite the following educational content to be clear, engaging, and concise:\n\n{input}"
        )
    prompt = prompt_template.replace("{input}", chapter_text)

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",  
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.7,
        "top_p": 0.9,
    }

    try:
        response = requests.post(
            "https://api.together.xyz/inference",
            json=data,
            headers=headers
        )
        response.raise_for_status()
        result = response.json()

        # Safely parse possible response structures
        if "output" in result:
            return result["output"].strip()
        elif "choices" in result and len(result["choices"]) > 0:
            return result["choices"][0].get("text", "").strip()
        else:
            print(f"[DEBUG] Unexpected response format: {result}")
            return "Error: Unexpected response format from Together API."

    except Exception as e:
        print(f"[ERROR] Together API failed: {e}")
        return "Error generating content."


def rewrite_chapter(chapter_text: str, prompt_template: str = None) -> str:
    return generate_content(chapter_text, prompt_template)
