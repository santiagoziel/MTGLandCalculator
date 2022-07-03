'''
takes in a mtggoldfish deck link and returns a dcit with its lands and the amout it has
'''

import requests
from bs4 import BeautifulSoup

from dta_pkt import r as redisdb

def get_lands_list(deck):
    headers = {
    "authority": "www.mtggoldfish.com",
    "method": "GET",
    "path": deck,
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "es-419,es;q=0.9",
    "user-agent": "Lands Calculation APP by santiagoziel"
    }

    response = requests.get(f'https://www.mtggoldfish.com{deck}#online',  headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table", {"class": "deck-view-deck-table"})
    cards = table.find_all("tr", {'class': None})
    list_of_lands = {}

    for card in cards:
        number = card.find("td", {'class':"text-right"}).string.strip()
        data = card.find("span", {'class':'card_id card_name'}).find("a").string.strip()
        info = redisdb.hgetall(data)
        #print(f"card: {data} has {number} copies is {'' if info[b'isLand'] == b'True' else 'not'} a land")
        if info[b'isLand'] == b'True':
            list_of_lands[data] = number
    return list_of_lands
