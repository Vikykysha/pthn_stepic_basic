import requests
import json

client_id = '...'
client_secret = '...'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
artist = []
with open('c','r') as f:
    for line in f:
        url = "https://api.artsy.net/api/artists/{}".format(line.strip())
        # инициируем запрос с заголовком
        r = requests.get(url, headers=headers)
        r.encoding = 'utf-8'

        # разбираем ответ сервера
        j = json.loads(r.text)
        name = j['sortable_name']
        year = j['birthday']
        artist.append((name, year))

for l in sorted(artist, key = lambda n : (n[1], n[0])):
    print(l[0].strip())