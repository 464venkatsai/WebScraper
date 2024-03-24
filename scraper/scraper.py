# Main scraper class and related functions

# Import Pre-requisites
import requests
from bs4 import BeautifulSoup
from .config import BASE_URL, TIMEOUT
from .utils import Log
import re
import pandas
from concurrent.futures import ThreadPoolExecutor


class Scraper:
    def __init__(self):
        Log.setup_logging()


    def exportScrapedData(self,data,format="csv",name="data"):
        # Exporting data in CSV, EXCEL AND JSON formats
        try:
            if format=="csv":
                pandas.DataFrame(data).to_csv(f"./data/{name}.csv")

            elif format=="xlsx":
                pandas.DataFrame(data).to_excel(f"./data/{name}.xlsx")

            elif format=="json":
                pandas.DataFrame(data).to_json(f"./data/{name}.json")

            else:
                Log.ERROR(f'{format} is not Supported')
                raise f"{format} Format is not Supported"
        # Logging Error
        except Exception as e:
            Log.ERROR(f'Export Error : {e}')



    def scrape_url(self, url,tag="",class_=""):
        try:
            # Getting the html document and making soup for further parsing
            document = requests.get(url, timeout=TIMEOUT)
            document.raise_for_status()
            soup = BeautifulSoup(document.content, 'html.parser')
            content = []
            # Finding according Tag and className
            for tag in soup.find_all(tag,class_=class_):
                # Preprocessing text like removing extra spaces and lines
                content.append(tag.text.replace("\n","").replace("  ",""))

            return content
        # Logging errors
        except Exception as e:
            Log.ERROR(f"Error scraping URL: {url}. {e}")
        # Logging that function terminated
        finally:
            Log.INFO(f"Scrape_url for {url} Ended")


    # Scraping from multiple urls using Threading to scrape parallely
    def scrape_multiple_urls(self, urls):
        dataUrls = []

        with ThreadPoolExecutor() as executor:
            # All Threads are submitted to executor and started at once
            futures = [executor.submit(self.scrape_url, url) for url in urls] 

            for future in futures:
                try:
                    # Storing all their future result in dataURls when thread is completed
                    dataUrls.append(future.result())

                except Exception as e:
                    Log.ERROR(f"Scraping Multiple Urls : Error retrieving data: {e}")

        # If data is needed in the list format
        return dataUrls

    