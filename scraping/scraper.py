from playwright.sync_api import sync_playwright
import os

def scrape_and_screenshot(url, save_folder="scraped_data"):
    os.makedirs(save_folder, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"Visiting: {url}")
        page.goto(url)
        
        # Save Screenshot
        screenshot_path = os.path.join(save_folder, "screenshot.png")
        page.screenshot(path=screenshot_path)
        print(f"✅ Screenshot saved at {screenshot_path}")

        # Save Page Content (Text)
        content = page.content()
        content_path = os.path.join(save_folder, "page.html")
        with open(content_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ HTML content saved at {content_path}")

        browser.close()

if __name__ == "__main__":
    test_url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
    scrape_and_screenshot(test_url)
