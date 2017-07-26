import requests

url_list = [
    'www.google.com',
    'www.bing.com',
]

# 1.For循环
for url in url_list:
    result = requests.get(url)
    print(result.text)