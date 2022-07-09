import redis,json

r = redis.Redis(host="db", port=6379, db=0)
basicLands = ["Forest", "Island", "Mountain", "Plains", "Swamp", "Snow-Covered Forest", "Snow-Covered Island", "Snow-Covered Mountain", "Snow-Covered Plains", "Snow-Covered Swamp"]
with open('cards/StandardAtomic.json', encoding="UTF-8") as f:
    data = json.load(f)
    for card in data["data"]:
        name = card.split(" // ")[0] #because i want full name for split cards
        #basic lands and similar dont have edhRank i jut give them 0
        try:
            rank = data["data"][f"{card}"][0]["edhrecRank"]
        except KeyError as e:
            rank = 0
        cost = ""
        isLand = False
        for face in data["data"][f"{card}"]:
            cost += face["manaCost"] if "manaCost" in face else ""
            isLand = isLand if not "Land" in face["type"] else True
        isBasic = name in basicLands
        print(name,rank,cost,isLand)
        card = {"manaCost":f"{cost}", "isLand":f"{isLand}", "isBasic":f"{isBasic}"}
        r.hmset(name, card)
