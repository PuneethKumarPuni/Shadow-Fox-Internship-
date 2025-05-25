# Task Web Scraper: Extract data from websites using libraries like Beautiful Soup or Scrapy. 

## Completed as part of Python Development Internship by Shadow Fox

### Objective:

# Web Scraper Project - Website Data Extraction

## Overview

This project demonstrates a simple web scraper implemented in Python using the `requests` and `BeautifulSoup` libraries. It extracts specific data from a website and saves the scraped information into a PDF file for easy viewing and analysis.

The scraper focuses on:

- Fetching web pages with HTTP requests.
- Parsing HTML content with BeautifulSoup.
- Extracting targeted data using CSS selectors.
- Saving the extracted data in a formatted PDF.
- Handling network and request errors gracefully.

## Features

- Scrapes data such as titles, descriptions, and menu items from web pages.
- Supports multiple elements per selector, storing lists when applicable.
- Generates a clean PDF report of the scraped data using the ReportLab library.
- Implements basic error handling to manage HTTP request failures.

## Technologies Used

- Python 3.x
- `requests` - for making HTTP requests.
- `BeautifulSoup` (bs4) - for parsing and extracting HTML content.
- `ReportLab` - for generating PDF documents.

## How It Works

1. Initialize the `WebScraper` class with the base URL of the target website.
2. Fetch the HTML content of the homepage or specified path.
3. Extract data based on given CSS selectors for elements like titles and navigation links.
4. Format and save the extracted data into a PDF file.
5. Print a success message upon PDF creation.

## Setup & Usage

1. Install required Python packages (preferably in a virtual environment):

   ```bash
   pip install requests beautifulsoup4 reportlab
   ```

2. Run the script:

   ```bash
   python scraper.py
   ```

3. The scraper will fetch data from the specified website and generate a PDF named `scraped_output.pdf` in the current directory.

## Customization

- Change the target website URL by modifying the `base_url` in the `WebScraper` initialization.
- Update the CSS selectors in the `selectors` dictionary to extract different or additional data from the target site.
- Modify the PDF formatting in the `save_to_pdf` method to customize the appearance of the output report.

## Error Handling

- The scraper uses try-except blocks to catch network errors such as connection issues or invalid responses.
- If the page fails to load, the program prints an error message and exits gracefully without crashing.

### Author:
Intern Puneeth Kumar P.
