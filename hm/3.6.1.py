import requests
import json

with open('d','r') as f:
    for line in f.readlines():
        url = 'http://numbersapi.com/{}/math?json=true'.format(line.strip())
        res = requests.get(url).text
        res = json.loads(res)
        if res['found'] == True:
            print('Interesting')
        else:
            print('Boring')