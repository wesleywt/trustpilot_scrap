from urllib.request import urlopen as request
from bs4 import BeautifulSoup as soup


def next(url):
    i = 1
    next_page = True

    while i <= 4:
        nexturl = f'{url}?page={i}'
        print(nexturl)

        r = request(nexturl)
        html = r.read()
        r.close()
        soup_page = soup(html, 'html.parser')
        review_title = soup_page.findAll('a', {'class': 'link link--large link--dark'})
        # review_titles =review_title[2].text
        reviews = []
        for review in review_title:
            reviews.append(review.text)
        i += 1
        return reviews




if __name__ == '__main__':
    pages = next(url='https://www.trustpilot.com/review/www.elegantthemes.com')
    print(pages)
    print(len(pages))
