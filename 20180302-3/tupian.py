import requests
from bs4 import BeautifulSoup
import re
import os

r = "http://tieba.baidu.com/p/2166231880"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
url = requests.get(r, headers=headers)
soup = BeautifulSoup(url.text, 'lxml')
content = soup.find_all('img')
list_of_pic = []
for i in content:
    pic_type = i.attrs.get('pic_type')
    if pic_type == '0':
        # print(i.attrs.get('src'))
        list_of_pic.append(i.attrs.get('src'))

for x in list_of_pic:
    # print(x)
    if os.path.isdir('./pic'):
        pass
    else:
        os.mkdir('./pic')
    # print(x[x.rfind('/') + 1:])
    pic_f = x[x.rfind('/') + 1:]
    # print(pic_f)
    pic = requests.get(x, headers=headers)
    with open('./pic/' + pic_f, 'wb') as file:
        file.write(pic.content)
    # print(pic.content)