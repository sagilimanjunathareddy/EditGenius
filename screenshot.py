from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

def capture_screenshot(output_path="output/screenshot.png"):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,3000")

       
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

        driver.get("http://localhost:8501")
        time.sleep(5)  

      
        original_size = driver.execute_script("return [document.body.scrollWidth, document.body.scrollHeight];")
        driver.set_window_size(original_size[0], original_size[1])
        time.sleep(2)

        if not os.path.exists("output"):
            os.makedirs("output")

        driver.save_screenshot(output_path)
        print(f"[✅] Screenshot saved at {output_path}")
        driver.quit()
        return output_path

    except Exception as e:
        print(f"[❌] Screenshot failed: {e}")
        return None
