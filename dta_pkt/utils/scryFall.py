import requests

response = requests.get(f"https://api.scryfall.com/cards/named?exact=Sunrise Cavalier")
data = response.json()
print(data)
