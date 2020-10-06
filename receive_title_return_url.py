import requests
from bs4 import BeautifulSoup


def receive_title_return_url(title):
    req = requests.get('https://www.google.com/search?q=' + title)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup.select('div.tAd8D')[0].text







