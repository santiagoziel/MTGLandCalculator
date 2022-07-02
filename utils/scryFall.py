import requests

r = requests.get(f"https://api.scryfall.com/cards/named?exact=Sunrise Cavalier")
data = r.json()
print(data)
