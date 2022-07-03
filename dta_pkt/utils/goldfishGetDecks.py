'''
gets a list of mtg goldfish decks that coointain certain cards
'''

import requests
from bs4 import BeautifulSoup
# TODO: get date range
# TODO: ask for format

format = "Standard"
#maybe ill put this on the redis db later on, for now i want it easy to edit
#4 color decks are very annoying to look for, ill think of somethinhg later on
deckNames = {
"U" : "Mono Blue",
"B" : "Mono Black",
"R" : "Mono Red",
"G" : "Mono Green",
"W" : "Mono White",
"UB": '"UB"+or+"Rackdos"',
"UR": '"UR"+or+"Izzet"',
"UG": '"UG"+or+"Simic"',
"UW": '"UW"+or+"Azorius"',
"BR": '"BR"+or+"Rakdos"',
"BG": '"BG"+or+"Golgari"',
"BW": '"BW"+or+"Orzhov"',
"RG": '"RG"+or+"Gruul"',
"RW": '"RW"+or+"Boros"',
"GW": '"GW"+or+"Selesnya"',
"BGW": "Abzan",
"UGW": "Bant",
"UBW": "Esper",
"UBR": "Grixis",
"URW": "Jeskai",
"BRG": "Jund",
"BRW": "Mardu",
"RGW": "Naya",
"UBG": "Sultai",
"URG": "Temur",
"UBRG": "UBRG",
"UBRW": "UBRW",
"UBGW":"UBGW",
"URGW":"URGW",
"BRGW":"BRGW",
"UBRGW":"5 color"
}
url = "https://www.mtggoldfish.com/deck_searches/create?"
def get_list_of_decks(coloridentity):
    payload = {
    "utf8" : "✓",
    "deck_search[name]" : deckNames[coloridentity],
    "deck_search[format]" : format,
    "deck_search[types][]": "user, tournament",
    "deck_search[player]":"",
    "deck_search[date_range]":"04/01/2022+-+07/01/2022",
    "counter":"2",
    "commit":"Search",
    "deck_search[deck_search_card_filters_attributes][0][card]":"",
    "deck_search[deck_search_card_filters_attributes][0][quantity]":"1",
    "deck_search[deck_search_card_filters_attributes][0][type]":"maindeck",
    }
    payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
    response = requests.get(url, params=payload_str)

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find("table", {"class": "table-striped"})
    rows =  table.find_all("tr")
    # for row in rows:
    #     a = row.find("a")
    #     if a != None:
    #         print(a['href'])
    listOfDecks = [row.find("a")['href'] for row in rows if row.find("a") != None]

    return listOfDecks
