import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit
from reportlab.lib import colors

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

    def save_to_pdf(self, data, filename):
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter
        margin = 50
        y = height - margin

        def draw_heading(text, size=16, space_after=20):
            nonlocal y
            if y < margin + 50:
                c.showPage()
                y = height - margin
            c.setFont("Helvetica-Bold", size)
            c.setFillColor(colors.darkblue)
            c.drawString(margin, y, text)
            y -= space_after
            c.setFillColor(colors.black)

        def draw_field(label, value, size=12, indent=20, space_after=15):
            nonlocal y
            if y < margin + 60:
                c.showPage()
                y = height - margin

            c.setFont("Helvetica-Bold", size)
            c.drawString(margin, y, f"{label}:")
            y -= 15
            c.setFont("Helvetica", size)

            if isinstance(value, list):
                for item in value:
                    lines = simpleSplit(item, "Helvetica", size, width - margin * 2 - indent)
                    for line in lines:
                        c.drawString(margin + indent, y, f"- {line}")
                        y -= 15
            elif value:
                lines = simpleSplit(value, "Helvetica", size, width - margin * 2 - indent)
                for line in lines:
                    c.drawString(margin + indent, y, line)
                    y -= 15
            else:
                c.drawString(margin + indent, y, "N/A")
                y -= 15
            y -= space_after

        draw_heading("Scraped Data from books.toscrape.com", size=18)

        for key, value in data.items():
            label = key.replace("_", " ").title()
            draw_field(label, value)

        c.save()
        print(f"PDF created successfully: {filename}")

def scrape_and_generate_pdf():
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
    scraper.save_to_pdf(scraped_data, "scraped_output.pdf")

if __name__ == "__main__":
    scrape_and_generate_pdf()
