# Main scraper class and related functions

# Import Pre-requisites
import requests
from bs4 import BeautifulSoup
from .config import BASE_URL, TIMEOUT
from .utils import Log
import re
import pandas

class Scraper:
    def __init__(self):
        Log.setup_logging()

    def REGEX(self,content:list,pattern=r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b'):
        for i in range(len(content)):
            content[i] = re.findall(pattern,content[i])
        return content
    def scrape_url(self, url,tag="",class_="",regex=True):
        try:
            document = requests.get(url, timeout=TIMEOUT)
            document.raise_for_status()
            soup = BeautifulSoup(document.content, 'html.parser')
            content = []
            for tag in soup.find_all(tag,class_=class_):
                content.append(tag.text.replace("\n","").replace("  ",""))
            return content

        except Exception as e:
            Log.ERROR(f"Error scraping URL: {url}. {e}")

        finally:
            Log.INFO(f"Scrape_url for {url} Ended")

    def scrape_multiple_urls(self, urls):
        results = []
        for url in urls:
            soup = self.scrape_url(url)
            if soup:
                results.append(soup)
        return results
    
    def exportScrapedData(self,data,format="csv"):
        try:
            if format=="csv":
                pandas.DataFrame(data).to_csv("./data/data.csv")
            elif format=="xlsx":
                pandas.DataFrame(data).to_excel("./data/data.xlsx")
            elif format=="json":
                pandas.DataFrame(data).to_json("./data/data.json")
            else:
                Log.ERROR(f'{format} is not Supported')
                raise f"{format} Format is not Supported"
        except Exception as e:
            Log.ERROR(f'Export Error : {e}')

