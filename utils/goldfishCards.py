import requests
headers = {
"authority": "www.mtggoldfish.com",
"method": "GET",
"path": "/deck/4911176",
"scheme": "https",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"accept-encoding": "gzip, deflate, br",
"accept-language": "es-419,es;q=0.9",
"user-agent": "Lands Calculation APP by santiagoziel"
}
r = requests.get('https://www.mtggoldfish.com/deck/4911176#online',  headers=headers)
print(r.text)
