import requests, json

#lands = [('Blightstep Pathway', 8), ('Clearwater Pathway', 8), ("Xander's Lounge", 8), ('Riverglide Pathway', 6), ('Haunted Ridge', 4)]
class Land:
    def __init__(self, name, age, image):
        self.name = name
        self.price = age
        self.image = image
    def __repr__(self):
        return f"Land(Name: {self.name}, Price: {self.price})"


def gen_display_info(lands):
    identifiers = [{"name": name[0]} for name in lands]

    reponse = requests.post("https://api.scryfall.com/cards/collection", json = {"identifiers":identifiers})

    data = json.loads(reponse.text)
    displayinfo = []
    for card in data['data']:
        if "card_faces" in card:
            displayCard = Land(card["name"], card["prices"]['usd'], card["card_faces"][0]["image_uris"]["normal"])
        else:
            displayCard = Land(card["name"], card["prices"]['usd'], card["image_uris"]["normal"])
        displayinfo.append(displayCard)
    return displayinfo
