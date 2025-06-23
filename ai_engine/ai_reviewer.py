from openai import OpenAI
import os

openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def rewrite_chapter(content, prompt_template):
    prompt = prompt_template.replace("{{content}}", content)
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional book rewriter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content