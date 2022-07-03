import requests

# response = requests.get(f"https://api.scryfall.com/cards/named?exact=Sunrise Cavalier")
# data = response.json()
# print(data)

params = {
  "identifiers": [
    {
      "name": "Blightstep Pathway"
    },
    {
      "name": "Clearwater Pathway"
    },
    {
      "name": "Xander's Lounge"
    },
    {
      "name": "Riverglide Pathway"
    }
  ]
}

reponse = requests.post("https://api.scryfall.com/cards/collection", json  = params)
print(reponse.text)
