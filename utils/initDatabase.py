
import json

with open('cards\sampleAtomic.json', encoding="UTF-8") as f:
    data = json.load(f)
    for card in data["data"]:
        for face in data["data"][f"{card}"]:
            if len(data["data"][f"{card}"]) > 1:
                print(f"Name: {face['faceName']}")
            else:
                print(f'Name: {face["name"]}')
            if not "Land" in face["type"]:
                print(f'Cost: {face["manaCost"]}')
                print("isLand: False")
            else:
                print(f'Cost: None')
                print("isLand: True")
            print(f'Rank: {face["edhrecRank"]}')
