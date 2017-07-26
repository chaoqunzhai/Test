import requests
from concurrent.futures import ThreadPoolExecutor

def fetch_request(url):
    result = requests.get(url)
    print(result.text)

pool = ThreadPoolExecutor(10)
url_list = [
    'www.google.com',
    'www.bing.com',
]
for url in url_list:
    # 去线程池中获取一个线程
    # 线程去执行fetch_request方法
    pool.submit(fetch_request,url)


pool.shutdown(True)

