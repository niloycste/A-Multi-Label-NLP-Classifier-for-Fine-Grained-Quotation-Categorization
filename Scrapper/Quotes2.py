import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from tqdm import tqdm
import time
import pandas as pd

def scrape_quotes(url):
   
    driver.get(url)
    time.sleep(3)  

   
    quote_elements = driver.find_elements(By.CLASS_NAME, "quote")

    quotes_data = []

    for quote_element in quote_elements:
        
        tags_element = quote_element.find_element(By.CLASS_NAME, "smallText")
        tags_text = tags_element.text if tags_element else ""
        tags = [tag.strip() for tag in tags_text.replace("tags:", "").split(',')]

        
        quote_text = quote_element.find_element(By.CLASS_NAME, "quoteText").text
        quote_text = quote_text.replace("“", "").replace("”", "").replace('"', "").replace("―", "")

        
        author = quote_element.find_element(By.CLASS_NAME, "authorOrTitle").text

        
        quotes_data.append({
            "author": author,
            "quotes": quote_text,
            "tags": tags
        })

    return quotes_data

def scrape_quotes_from_urls(urls):
    all_quotes_data = []

    for url in urls:
        for idx in tqdm(range(1, 101)):  # Iterate through all 100 pages
            page_url = f"{url}?page={idx}"
            quotes_data = scrape_quotes(page_url)
            all_quotes_data.extend(quotes_data)

    return all_quotes_data

if __name__ == "__main__":
    gecko_path = r'D:\Mastercourse\Book Scrapper\driver\geckodriver.exe'
    service = Service(gecko_path)
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(service=service, options=options)

    urls_to_scrape = [
        # "https://www.goodreads.com/quotes/tag/humor",
        # "https://www.goodreads.com/quotes/tag/philosophy",
        # "https://www.goodreads.com/quotes/tag/inspirational",
        # "https://www.goodreads.com/quotes/tag/hope",
        # "https://www.goodreads.com/quotes/tag/life",
        # "https://www.goodreads.com/quotes/tag/faith"
        #   "https://www.goodreads.com/quotes/tag/love",
        #   "https://www.goodreads.com/quotes/tag/happiness"
            "https://www.goodreads.com/quotes/tag/poetry",
            "https://www.goodreads.com/quotes/tag/success",
            "https://www.goodreads.com/quotes/tag/science"


    ]

    all_quotes_data = scrape_quotes_from_urls(urls_to_scrape)

    
    df = pd.DataFrame(all_quotes_data)
    df.to_csv("latest_data.csv", index=False)

   
    driver.quit()
