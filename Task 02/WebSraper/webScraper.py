import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def get_page(self, path="/"):
        full_url = urljoin(self.base_url, path)
        try:
            response = self.session.get(full_url, headers=self.headers)
            response.raise_for_status()
            return BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            print("Failed to fetch page:", e)
            return None

    def extract_data(self, soup, selectors):
        data = {}
        for key, selector in selectors.items():
            elements = soup.select(selector)
            if not elements:
                data[key] = None
            elif len(elements) == 1:
                data[key] = elements[0].get_text(strip=True)
            else:
                data[key] = [el.get_text(strip=True) for el in elements]
        return data

    def save_to_csv(self, data, filename):
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Field', 'Value'])

                for key, value in data.items():
                    label = key.replace("_", " ").title()
                    if isinstance(value, list):
                        value_str = ', '.join(value)
                    elif value:
                        value_str = value
                    else:
                        value_str = "N/A"
                    writer.writerow([label, value_str])
            print(f"CSV file created successfully: {filename}")
        except Exception as e:
            print("Failed to write CSV:", e)

def scrape_and_generate_csv():
    scraper = WebScraper("https://books.toscrape.com/")
    soup = scraper.get_page("/")
    if not soup:
        return

    selectors = {
        "title": "div.page-header h1",
        "description": "p",
        "menu_items": "ul.nav-list li a"
    }

    scraped_data = scraper.extract_data(soup, selectors)
    scraper.save_to_csv(scraped_data, "scraped_output.csv")

if __name__ == "__main__":
    scrape_and_generate_csv()
