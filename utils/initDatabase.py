
import json

with open('cards\sampleAtomic.json', encoding="UTF-8") as f:
    data = json.load(f)
    for card in data["data"]:
        print("-----------")
        print(f"Cheking {card}")
        for face in data["data"][f"{card}"]:
            if not "Land" in face["type"]:
                continue
            if len(data["data"][f"{card}"]) > 1:
                print(f"FaceName: {face['faceName']}")
            print(face["colorIdentity"])
            print(face["text"])
            print(face["type"])
        print("-----------")
