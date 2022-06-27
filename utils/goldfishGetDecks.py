import requests

url = "https://www.mtggoldfish.com/deck_searches/create?utf8=✓"
payload = {
"deck_search[name]" : "",
"deck_search[format]" : "pioneer",
"deck_search[types][]": "tournament, user",
"deck_search[player]":"",
"deck_search[date_range]":"06/13/2022+-+06/27/2022",
"deck_search[deck_search_card_filters_attributes][0][card]":"Young+Pyromancer",
"deck_search[deck_search_card_filters_attributes][0][quantity]":"4",
"deck_search[deck_search_card_filters_attributes][0][type]":"maindeck",
"deck_search[deck_search_card_filters_attributes][1][card]":"",
"deck_search[deck_search_card_filters_attributes][1][quantity]":"1",
"deck_search[deck_search_card_filters_attributes][1][type]":"maindeck",
"counter":"2",
"commit":"Search"
}
payload_str = "&".join("%s=%s" % (k,v) for k,v in payload.items())
r = requests.get(url, params=payload_str)

with open("response.html", "w") as f:
    f.write(r.text)
