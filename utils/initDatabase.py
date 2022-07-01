import redis,json

r = redis.Redis(host="localhost", port=6379, db=0)

with open('../cards/sampleAtomic.json', encoding="UTF-8") as f:
    data = json.load(f)
    for card in data["data"]:
        name = card.split(" // ")[0] #because i want full name for split cards
        rank = data["data"][f"{card}"][0]["edhrecRank"]
        cost = ""
        isLand = False
        for face in data["data"][f"{card}"]:
            cost += face["manaCost"] if "manaCost" in face else ""
            isLand = isLand if not "Land" in face["type"] else True

        print(name,rank,cost,isLand)
        card = {"manaCost":f"{cost}", "isLand":f"{isLand}", "edhrank":rank}
        r.hmset(name, card)
