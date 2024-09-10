import requests

import json

from pprint import pprint

# 1 Получаем информацию о картине дня.

nasa_url = 'https://api.nasa.gov/planetary/apod'
params = {
    'api_key': 'Fkj7ZEx6zWfRQeNpfcMjeXfYt7y39IrCr3URbq5w',
    'date': '2024-01-01'
}
response = requests.get(nasa_url, params=params)
print(response.text)

pprint(response.json())
image_url = response.json()['url']
# print(image_url)

# 2 Скачать картину дня
response = requests.get(image_url)
with open('image.jpg', 'wb') as f:
    f.write(response.content)

# 3 Просмотр картины 1 января ('date': '2024-01-01')

