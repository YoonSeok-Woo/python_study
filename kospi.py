import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text # 요청 보내고 받은 응답 text로 변환
data = BeautifulSoup(response, 'html.parser')
kospi = data.select_one('#KOSPI_now')
change = data.select_one('#KOSPI_change')
result = kospi.text
res2 = change.text

print(f'현재 코스피 지수는  {result}입니다.')
print(f'변화율은 {res2}입니다.')