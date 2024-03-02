import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import random, time

HOST = 'https://www.kinopoisk.ru/'
URL = 'https://www.kinopoisk.ru/film/435/'
# URL = 'https://www.kinopoisk.ru/lists/movies/top250/?page=2'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
}

def get_data(url):
    r = requests.get(url, headers=HEADERS)
    r.encoding = 'utf8'
    
    # # with open('index.html', 'w') as f:
    # #     f.write(r.text)

    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find('div.styles_column__1Xp_v.styles_md_11__1AC7s.styles_lg_15__oinEq')
    # items = soup.find('div', class_='styles_root__1yOnb styles_topLine__3IBhC')
    # items = soup.find('div', attrs={'data-test-id': 'styles_column__1Xp_v styles_md_11__1AC7s styles_lg_15__oinEq'})
    
    print('11111111111111111111111111111111111111111111111111111111')
    print(items)


def get_data_with_selenium(url):
    # global name
    options = webdriver.FirefoxOptions()
    options.set_preference('general.useragent.override', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36')
    try:
        driver = webdriver.Firefox(
            executable_path='/Users/kamilkusakov/Downloads',
            options=options
        )
        time.sleep(s)
        driver.get(url=url)
        s = random.randrange(4, 7)
        time.sleep(s)
        
        with open('index_with_selenium.html', 'r') as f:
            f.write(driver.page_source)
            
        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

def main():
    get_data(URL)
    # get_data_with_selenium(URL)
    
if __name__ == '__main__':
    main() 