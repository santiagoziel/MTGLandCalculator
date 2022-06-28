with open("Deck - Obunn upgrades.txt", "r") as txt_file:
    file_content = txt_file.read()
    content_list = file_content.split("\n")
    content_list = content_list [:-2]
    for x in content_list:
        for card in range(int(x[:2])):
            print(f"{x[2:]}")
