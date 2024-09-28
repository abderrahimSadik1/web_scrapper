from bs4 import BeautifulSoup
import requests

def scrape_cnbc():
# URL of the page to be scraped
    URL = 'https://www.cnbc.com/technology/'

    # Send a GET request to the URL
    response = requests.get(URL)

    soup = BeautifulSoup(response.text, 'lxml')

    articles_title = soup.find_all('a', class_='Card-title')
    return articles_title

