import requests
from bs4 import BeautifulSoup

url_base = 'http://www.wydy8.com/'
respone = requests.get(url_base)
html = respone.text

obj = BeautifulSoup(html,'html.parser')

tag = obj.find(name='div',id='navbar' )

li_list = tag.find_all(name='li')


for i in li_list:
    i_obj = i.find(name='a')

    if len(i_obj.attrs.get('href')) > 2:
        aa=i_obj.attrs.get('href')
        aa = aa.strip('//')
        url_2= url_base + aa
        respone_1 = requests.get(url_2)
        print(respone_1.text)


replaceWith("<input></input");