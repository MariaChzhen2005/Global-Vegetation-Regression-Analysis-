import requests
from bs4 import BeautifulSoup

"""
BeautifulSoup scans page for links, iterates over them
Goal is to download every 28th link that ends with .nc
Url of scanned page is https://www.ncei.noaa.gov/data/avhrr-land-normalized-difference-vegetation-index/access/2007/
"""

def findLinks(url):
    page = requests.get(url).content
    bsObj = BeautifulSoup(page, 'html.parser')
    maybe_directories = bsObj.findAll('a', href=True)
    

    for day in range(len(maybe_directories)):
        print("day: ",day)
        for link in maybe_directories:
            if link['href'].endswith('.nc') and day%28==0:
                    print("LINK SATISFIES THE CONDITIONS. Day: ", day)
                    filename = maybe_directories[day].get('href')
                    url = 'https://www.ncei.noaa.gov/data/avhrr-land-normalized-difference-vegetation-index/access/2007/'+filename
                    print(filename)
                    r = requests.get(url, allow_redirects=True)
                    open(filename, 'wb').write(r.content)
                    break

startUrl = "https://www.ncei.noaa.gov/data/avhrr-land-normalized-difference-vegetation-index/access/2007/"
findLinks(startUrl)
