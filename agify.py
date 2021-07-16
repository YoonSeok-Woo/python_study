import requests
from bs4 import BeautifulSoup

name = 'Yoon'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()
url2 = f'https://api.nationalize.io/?name={name}'
nresp = requests.get(url2).json()
print('나이는 ',response['age'],'살 이실 것 같고..')
print('국적은 ',nresp['country'][0]['country_id'],'이실 것 같네요')
