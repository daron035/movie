import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import random, time

HOST = 'https://www.kinopoisk.ru/'
URL = 'https://www.kinopoisk.ru/lists/movies/top250/?page={p}'
# URL = 'https://www.kinopoisk.ru/lists/movies/top250/?page=2'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}

def get_data():
    urls = []
    # a = ''
    for p in range(1, 6):
        print(p)
        url = f'https://www.kinopoisk.ru/lists/movies/top250/?page={p}'
        r = requests.get(url, headers=HEADERS)
        r.encoding = 'utf8'
        time.sleep(3)

        soup = BeautifulSoup(r.text, 'lxml')
        items = soup.find_all('div', class_='styles_root__3a8vf')

        for items_url in items:
            items_url = items_url.find('a', class_='base-movie-main-info_link__3BnCh').get('href')
            urls.append('https://www.kinopoisk.ru' + items_url)
            print('https://www.kinopoisk.ru' + items_url)
            
            # a.join('https://www.kinopoisk.ru' + items_url)
    
    return urls



def main():
    get_data()
    
    # try:
    #     with open('index.txt', 'w') as f:
    #         f.write(a.split())
    # except:
    #     print(Exception)

    
if __name__ == '__main__':
    main() 