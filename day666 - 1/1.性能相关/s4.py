"""
线程多，并且在阻塞过程中无法执行其他任务

协程：微线程
非阻塞：不等,无论是否报错
异步：回调，通知
"""
# 1. asycio模块
# import asyncio
#
# @asyncio.coroutine
# def func1():
#     print('before...func1......')
#     yield from asyncio.sleep(5) # 变成Http请求
#     print('end...func1......')
#
#
# tasks = [func1(), func1()]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()
#
# import asyncio
#
#
# @asyncio.coroutine
# def fetch_async(host, url='/'):
#     print(host, url)
#     # 连接
#     reader, writer = yield from asyncio.open_connection(host, 80)
#
#     request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)
#     request_header_content = bytes(request_header_content, encoding='utf-8')
#
#     writer.write(request_header_content)
#     yield from writer.drain()
#     text = yield from reader.read()
#     print(host, url, text)
#     writer.close()
#
# tasks = [
#     fetch_async('www.cnblogs.com', '/wupeiqi/'),
#     fetch_async('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091')
# ]
#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()
#
# import asyncio
# import requests
#
#
# @asyncio.coroutine
# def fetch_async(func, *args):
#     print(args)
#     loop = asyncio.get_event_loop()
#     future = loop.run_in_executor(None, func, *args)
#     response = yield from future
#     print(response.url, response.content)
#
#
# tasks = [
#     fetch_async(requests.get, 'http://www.cnblogs.com/wupeiqi/'),
#     fetch_async(requests.get, 'http://dig.chouti.com/pic/show?nid=4073644713430508&lid=10273091')
# ]
#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()


# 2. gevent

# 3. Twisted
from twisted.web.client import getPage, defer
from twisted.internet import reactor

def all_done(arg):
    reactor.stop()

def callback(contents):
    print(contents)

deferred_list = []
url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(callback)
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)

reactor.run()


# 4. Tornado







# import gevent
#
# import requests
# from gevent import monkey
# monkey.patch_all()
#
#
# def fetch_async(method, url, req_kwargs):
#     print(method, url, req_kwargs)
#     response = requests.request(method=method, url=url, **req_kwargs)
#     print(response.url, response.content)
#
# # ##### 发送请求 #####
# gevent.joinall([
#     gevent.spawn(fetch_async, method='get', url='https://www.python.org/', req_kwargs={}),
#     gevent.spawn(fetch_async, method='get', url='https://www.yahoo.com/', req_kwargs={}),
#     gevent.spawn(fetch_async, method='get', url='https://github.com/', req_kwargs={}),
# ])