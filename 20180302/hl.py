# -*- coding=utf-8 -*-

import requests
from bs4 import BeautifulSoup

r = "http://web.gaore.com"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
url = requests.get(r, headers=headers)
soup = BeautifulSoup(url.text, 'html.parser')
article = soup.find_all('a')
for u in article:
    print(u['href'])