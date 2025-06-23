from fastapi import APIRouter
from scraping.scraper import fetch_text_from_url

router = APIRouter()

@router.get("/scrape")
def scrape(url: str):
    return {"content": fetch_text_from_url(url)}