import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

url = "https://www.kinopoisk.ru/lists/movies/top250/"
r = requests.get(url)
r.text
soup = BeautifulSoup(r.text, 'lxml')

link = "https://www.kinopoisk.ru" + soup.find('div', class_= 'styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').get('href')
print(link)
rus_name = soup.find('div', class_= 'styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
print(rus_name)
ang_name = soup.find('div', class_= 'styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
print(ang_name)
inf = soup.find('div', class_= 'styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('div', class_='desktop-list-main-info_additionalInfo__Hqzof').text
print(inf)


data = []

for p in range(1, 2):
    print(p)
    url = f"https://www.kinopoisk.ru/lists/movies/top250/?page={p}"
    r = requests.get(url)
    sleep(2)
    soup = BeautifulSoup(r.text, 'lxml')

    films = soup.findAll('div', class_='styles_root__ti07r')
    print(len(films))
    for film in films:
        link = "https://www.kinopoisk.ru" + film.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
        rus_name = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
        ang_name = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_secondaryText__M_aus').text
        inf = film.find('a', class_='base-movie-main-info_link__YwtP1').find('div',class_='desktop-list-main-info_additionalInfo__Hqzof').text
        data.append([link, rus_name, ang_name, inf])
print(data)

header = ['link', 'rus_name', 'ang_name', 'inf']
df = pd.DataFrame(data, columns = header)
df.to_csv('kinopoisk_data.csv',sep=';', encoding = 'utf8')
