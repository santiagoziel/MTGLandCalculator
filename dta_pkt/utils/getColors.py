import requests, re, time

from dta_pkt import app, r


def checkColors(name):

    if "Land" in data["type_line"]:
        return "L"
    mana_cost = data["mana_cost"]
    manaString = ''.join(str(item) for item in mana_cost)

    return re.sub('[\{\}1-9]',"",manaString)


def gen_color_identity(deckName):
    L = 0
    colors = {
    "U" : 0,
    "B" : 0,
    "R" : 0,
    "G" : 0,
    "W" : 0,
    }
    print("-----------------------------")
    print(deckName)
    print("-----------------------------")
    with open(app.config["UPLOAD_FOLDER"] + deckName, "r") as txt_file:
        file_content = txt_file.read()
        content_list = file_content.split("\n")
        #mtggoldfish adds two blank lines at the end of deck files for some reason
        #so here i remove them
        while("" in content_list) :
            content_list.remove("")

        for entry in content_list:
            amount, name = entry.split(" ",1)
            print(name)
            info = r.hgetall(name)
            #print(f"Amount: {amount}, card {name} {info[b'isLand']}")
            symbols = re.sub('[\{\}1-9]','',info[b'manaCost'].decode('utf-8'))
            print(f"{name} has symbols {symbols}")
            amount = int(amount)
            sum = 0
            for key in colors:
                colors[key] += symbols.count(key) * amount
                sum += colors[key]

            L += amount if info[b'isLand'] == b'True' else 0

    coloridentity = ""
    [coloridentity := coloridentity + key for key in colors if colors[key] != 0]

    return colors, L, coloridentity, sum
