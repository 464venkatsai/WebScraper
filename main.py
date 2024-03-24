from scraper.scraper import Scraper
from bs4 import BeautifulSoup
import requests
import pandas as pd
# # Create an instance of the Scraper
scraper = Scraper()

# # List of URLs to scrape (enclosed within square brackets to form a list)
urls = ['https://www.scrapethissite.com/pages/simple/']

# # Scrape the URL
countries = scraper.scrape_url(urls[0],tag="h3",class_="country-name")
capital = scraper.scrape_url(urls[0],tag="span",class_="country-capital")
population = scraper.scrape_url(urls[0],tag="span",class_="country-population")
area = scraper.scrape_url(urls[0],tag="span",class_="country-area")

data = {
    "Countries":countries,
    "Captial":capital,
    "Population":population,
    "Area (Km2)":area
}
scraper.exportScrapedData(data,format='csv')
scraper.exportScrapedData(data,format='xlsx')
scraper.exportScrapedData(data,format='json')