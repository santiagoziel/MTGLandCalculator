import requests, json

#lands = [('Blightstep Pathway', 8), ('Clearwater Pathway', 8), ("Xander's Lounge", 8), ('Riverglide Pathway', 6), ('Haunted Ridge', 4)]

def gen_display_info(lands):
    identifiers = [{"name": name[0]} for name in lands]

    reponse = requests.post("https://api.scryfall.com/cards/collection", json = {"identifiers":identifiers})

    data = json.loads(reponse.text)
    displayinfo = []
    for card in data['data']:
        displayCard =[card["name"],card["prices"]['usd']]
        if "card_faces" in card:
            displayCard.append(card["card_faces"][0]["image_uris"]["normal"])
        else:
            displayCard.append(card["image_uris"]["normal"])
        displayinfo.append(displayCard)
    return displayinfo
