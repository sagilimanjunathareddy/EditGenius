# utils/screenshot.py

from playwright.sync_api import sync_playwright
import os

def take_screenshot(url: str, save_path: str = "screenshot.png") -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.screenshot(path=save_path, full_page=True)
        browser.close()
    return os.path.abspath(save_path)
