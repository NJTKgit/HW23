import requests
from bs4 import BeautifulSoup
import pandas as pd
def collect_user_rates(user_login):
    data = []
    while True:
        url = f'https://www.kinopoisk.ru/user/{user_login}/votes/'
        html_content = requests.get(url)

        soup = BeautifulSoup(html_content.text, 'lxml')

        entries = soup.find_all('div', class_='item')
        if len(entries) == 0:
            break
        for entry in entries:
            td_film_details = entry.find('div', class_='nameRus')
            film_name = td_film_details.find('a').text
            my_rating = entry.find('div', class_='vote').text
            avg = entry.find('div', class_='rating')
            avg_rating = avg.find('b').text
            data.append({'Название': film_name, 'Оценка пользователя': my_rating, "Средний рейтинг": avg_rating})
        return data
user_rates = collect_user_rates('217658719')
df = pd.DataFrame(user_rates)
df.to_excel('user_rates.xlsx')