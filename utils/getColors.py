import requests, re, time,redis

r = redis.Redis(host="localhost", port=6379, db=0)

def checkColors(name):

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

with open("../decks/Deck - redis deck test.txt", "r") as txt_file:
    file_content = txt_file.read()
    content_list = file_content.split("\n")
    #mtggoldfish adds two blank lines at the end of deck files for some reason
    #so here i remove them
    while("" in content_list) :
        content_list.remove("")
    for entry in content_list:
        amount, name = entry.split(" ",1)
        info = r.hgetall(name)
        print(f"Amount: {amount}, card {name} {info[b'isLand']}")
        symbols = re.sub('[\{\}1-9]','',info[b'manaCost'].decode('utf-8'))
        amount = int(amount)
        R += symbols.count("R") * amount
        G += symbols.count("G") * amount
        W += symbols.count("W") * amount
        U += symbols.count("U") * amount
        B += symbols.count("B") * amount
        L += amount if info[b'isLand'] == b'True' else 0

sum = R+G+W+U+B
print(f"R{R} G{G} W{W} U{U} B{B} sum{sum}")

print(f"Tierras: {L}")
print(f"R: {(R*L)/sum}")
print(f"G: {(G*L)/sum}")
print(f"W: {(W*L)/sum}")
print(f"U: {(U*L)/sum}")
print(f"B: {(B*L)/sum}")
