import requests
from bs4 import BeautifulSoup
import csv

CSV = 'dannie.csv'
HOST = 'https://www.kinopoisk.ru/'
URL ='https://www.kinopoisk.ru/lists/movies/top250/'
HEADERS = {
    'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
#Выполняем запрос на кинопоиск и говорим что пытаемся извлечь данные
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='styles_root__ti07r')
    spisok = []
    for item in items:
        spisok.append(
            {
                'Rus_name' : item.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').get_text(),
                'Ang_name' : item.find('a',class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').get_text(),
                'Link' : HOST + item.find('a',class_='base-movie-main-info_link__YwtP1').get('href')
            }
        )
    return spisok
    #Раскоментить при проверке, должен появится список. На этом этапе все работает.
    #print(spisok)

#Проверка функций get_html и get_content
#html = get_html(URL)
#get_content(html.text)

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Rus_name', 'Ang_name', 'link'])
        for item in items:
            writer.writerow([item['Rus_name'], item['Ang_name'], item['Link']])

def parser():
    PAGENATION = input('Введите колличество страниц для парсинга: ')
    PAGENATION = int(PAGENATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        spisok =[]
        for page in range(1, PAGENATION):
            print(f'Идет парсинг страницы: {page}')
            html = get_html(URL, params={'page' : page})
            spisok.extend(get_content(html.text))
            save_doc(spisok, CSV)
        pass
    else:
        print('Error')

parser()
