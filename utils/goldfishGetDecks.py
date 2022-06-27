'''
gets a list of mtg goldfish decks that coointain certain cards
'''

import requests
from bs4 import BeautifulSoup
url = "https://www.mtggoldfish.com/deck_searches/create?"
payload = {
"utf8" : "✓",
"deck_search[name]" : "",
"deck_search[format]" : "pioneer",
"deck_search[types][]": "tournament",
"deck_search[player]":"",
"deck_search[date_range]":"06/13/2022+-+06/27/2022",
"counter":"7",
"commit":"Search",
"deck_search[deck_search_card_filters_attributes][0][card]":"Elvish+Mystic",
"deck_search[deck_search_card_filters_attributes][0][quantity]":"4",
"deck_search[deck_search_card_filters_attributes][0][type]":"maindeck",
"deck_search[deck_search_card_filters_attributes][2][card]":"Llanowar+Elves",
"deck_search[deck_search_card_filters_attributes][2][quantity]":"4",
"deck_search[deck_search_card_filters_attributes][2][type]":"maindeck"
}
payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
r = requests.get(url, params=payload_str)

soup = BeautifulSoup(r.text, 'html.parser')
table = soup.find("table", {"class": "table-striped"})
rows =  table.find_all("tr")
for row in rows:
    a = row.find("a")
    if a != None:
        counter += 1
        print(a['href'])
