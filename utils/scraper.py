# utils/scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_wikipedia_content(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from paragraph tags
        paragraphs = soup.select('p')
        text = '\n'.join([p.get_text() for p in paragraphs[:10]])  # Get first 10 paragraphs
        return text.strip()
    except Exception as e:
        print(f"[ERROR] Failed to scrape content: {e}")
        return "Error scraping content."
