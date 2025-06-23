import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

       
        paragraphs = soup.find_all("p")
        content = "\n".join(p.get_text() for p in paragraphs[:10])  # Limit to 10 paras
        return content.strip()
    except Exception as e:
        print(f"[ERROR] Failed to scrape website: {e}")
        return "Error fetching content from the provided URL."
