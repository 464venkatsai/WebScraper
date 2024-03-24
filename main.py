from scraper.scraper import Scraper

scraper = Scraper()

urls = ['https://www.scrapethissite.com/pages/simple/']

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

# If need Export this by using exportScrapedData() 
# args - data , format , name 
# scraper.exportScrapedData(data,format='csv')
# scraper.exportScrapedData(data,format='xlsx')
# scraper.exportScrapedData(data,format='json')