import requests
from bs4 import BeautifulSoup as soup
import lxml
import pandas as pd


def soup_url(url):
    r = request(url)
    html = r.read()
    r.close()
    soup_page = soup(html, 'html.parser')
    return soup_page

if __name__ == '__main__':
    soup_page = soup_url(url='https://www.trustpilot.com/review/www.elegantthemes.com?page=2')
    print(soup_page)
