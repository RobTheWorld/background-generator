import requests
from bs4 import BeautifulSoup

# testing git update
res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find(id='score_38851337'))

