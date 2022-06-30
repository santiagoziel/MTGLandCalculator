import requests, re, time

def checkColors(name):
    r = requests.get(f"https://api.scryfall.com/cards/named?exact={name}")
    data = r.json()
    if "Land" in data["type_line"]:
        return "L"
    mana_cost = data["mana_cost"]
    manaString = ''.join(str(item) for item in mana_cost)

    return re.sub('[\{\}1-9]',"",manaString)

R = 0
G = 0
W = 0
U = 0
B = 0
L = 0
with open("decks\Deck - Obunn upgrades.txt", "r") as txt_file:
    file_content = txt_file.read()
    content_list = file_content.split("\n")
    content_list = content_list [:-2]
    for x in content_list:
        for card in range(int(x[:2])):
            time.sleep(.11)
            symbols = checkColors(f"{x[2:]}")
            R += symbols.count("R")
            G += symbols.count("G")
            W += symbols.count("W")
            U += symbols.count("U")
            B += symbols.count("B")
            L += symbols.count("L")

sum = R+G+W+U+B
print(f"R{R} G{G} W{W} U{U} B{B} sum{sum}")

print("Tierras:")
print(f"R: {(R*L)/sum}")
print(f"G: {(G*L)/sum}")
print(f"W: {(W*L)/sum}")
print(f"U: {(U*L)/sum}")
print(f"B: {(B*L)/sum}")
