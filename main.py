import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
import lxml
import json

url = 'https://www.trustpilot.com/review/www.elegantthemes.com'
reviews = {
        'Full Name': [],
        'Date': [],
        'Star Rating': [],
        'Headline of Review': [],
        'Body of Review': []
    }



def export_table_print(reviews):
    table = pd.DataFrame(reviews, columns=['Full Name', 'Date', 'Star Rating', 'Headline of Review', 'Body of Review'])
    table.index = table.index + 1
    table.to_csv(f'reviews.csv', sep=',', encoding='utf-8', index=False)


def get_reviews(bs):
    review_card = bs.findAll('div', class_="review-card")


    for i in range(len(review_card)):
        review_info = review_card[i].find('script', {'data-initial-state': 'review-info'})
        review_date = review_card[i].find('script', {'data-initial-state': 'review-dates'})
        review_info_json = json.loads(review_info.text)
        date_json = json.loads(review_date.text)
        date = date_json['publishedDate']
        name = review_info_json['consumerName']
        company = review_info_json['businessUnitDisplayName']
        stars = review_info_json['stars']
        # Added this in case no title is provided.
        if review_card[i].find('a', {'class': 'link link--large link--dark'}).text == None:
            review_title = 'No title provided'
        else:
            review_title = review_card[i].find('a', {'class': 'link link--large link--dark'}).text

        # Some reviews have comments left out leading to the NoneType Error. Replaced it with if check
        if review_card[i].find('p', {'class': 'review-content__text'}) == None:
            review_comment = 'No comment provided'
        else:
            review_comment = review_card[i].find('p', {'class': 'review-content__text'}).text.strip()

        reviews['Full Name'].append(name)
        reviews['Date'].append(date)
        reviews['Star Rating'].append(stars)
        reviews['Headline of Review'].append(review_title)
        reviews['Body of Review'].append(review_comment)


def parse_page(next_url):
    i = 147
    next_page = True

    while i <= 152 and next_page:
        nexturl = f'{url}?page={i}'
        print(nexturl)


        page = requests.get(nexturl)
        if page.status_code == requests.codes.ok:
            bs = soup(page.text, "lxml")
            next_page = bs.findAll('a', {'data-page-number': 'next-page'})
            get_reviews(bs)
            export_table_print(reviews)
        i += 1



parse_page(url)

















