import requests

import json

from pprint import pprint

# 1 Получаем информацию о картине дня.

nasa_url = 'https://api.nasa.gov/planetary/apod'
params = {
    'api_key': 'Fkj7ZEx6zWfRQeNpfcMjeXfYt7y39IrCr3URbq5w'
}
response = requests.get(nasa_url, params=params)
print(response.text)

pprint(response.json())
image_url = response.json()['url']
# print(image_url)

# 2 Скачать картину дня
