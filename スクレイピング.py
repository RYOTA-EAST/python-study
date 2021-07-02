from bs4 import BeautifulSoup
import requests

# アクセスしてデータを全て変数に格納
html = requests.get('https://www.python.org')
soup = BeautifulSoup(html.text, 'lxml')

# titleを探し出して表示
titles = soup.find_all('title')
print(titles[0].text)

# classがintroductionのdivを探して表示
intro = soup.find_all('div', {'class': 'introduction'})
print(intro[0].text)