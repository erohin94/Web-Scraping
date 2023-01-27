import requests
import math

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0',
}

response = requests.get(
    'https://production.dataviz.cnn.io/index/fearandgreed/graphdata',
    headers=headers,
)
items = response.json()['fear_and_greed']['score']
print(math.ceil(items))
