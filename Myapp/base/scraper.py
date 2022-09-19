
import requests
from bs4 import BeautifulSoup
import lxml
def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
        "Accept-Language": "en",
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    try:
        name = soup.select_one(selector="#productTitle").getText()
        name = name.strip()
    except:
        name=''
    try:
        price = soup.select_one(selector=".a-offscreen").getText()
        price = float(price[1:])
    except:
        price=''
    try:
        rating = soup.select_one(selector=".a-icon-alt").getText()
    except:
        rating = ''

    try:
        details = soup.select_one(selector=".a-size-base").getText()
    except:
        details = ''

    return name, price, rating, details