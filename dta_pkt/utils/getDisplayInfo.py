import requests, json, math

#lands = [('Blightstep Pathway', 8), ('Clearwater Pathway', 8), ("Xander's Lounge", 8), ('Riverglide Pathway', 6), ('Haunted Ridge', 4)]
class Land:
    def __init__(self, name, age, image, column, row):
        self.name = name
        self.price = age
        self.image = image
        self.column = column
        self.row = row
    def __repr__(self):
        return f"Land(Name: {self.name}, Price: {self.price})"


def gen_display_info(lands):
    identifiers = [{"name": name[0]} for name in lands]

    reponse = requests.post("https://api.scryfall.com/cards/collection", json = {"identifiers":identifiers})

    data = json.loads(reponse.text)
    displayinfo = []
    for index, card in enumerate(data['data'], start=1):
        #calculating row and column for display
        desired_columns = 3
        row = math.ceil(index/desired_columns)
        column = index -((row - 1) * desired_columns)
        if "card_faces" in card:
            displayCard = Land(card["name"], card["prices"]['usd'], card["card_faces"][0]["image_uris"]["normal"], column, row)
        else:
            displayCard = Land(card["name"], card["prices"]['usd'], card["image_uris"]["normal"], column, row)
        displayinfo.append(displayCard)
    return displayinfo
