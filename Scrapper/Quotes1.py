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

if __name__ == "__main__":
    gecko_path = r'D:\Mastercourse\Book Scrapper\driver\geckodriver.exe'
    service = Service(gecko_path)
    options = Options()
    options.headless = False
    driver = webdriver.Firefox(service=service, options=options)
    
    base_url = "https://www.goodreads.com/quotes/tag/truth"

    all_quotes_data = []

    for idx in tqdm(range(100)):
        page_no = idx + 1
        page_url = f"{base_url}?page={page_no}"
        quotes_data = scrape_quotes(page_url)
        all_quotes_data.extend(quotes_data)

   
    df = pd.DataFrame(all_quotes_data)
    df.to_csv("truth.csv", index=False)

    
    driver.quit()
