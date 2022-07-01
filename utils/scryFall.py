import requests

r = requests.get(f"https://api.scryfall.com/cards/named?exact={name}")
data = r.json()
