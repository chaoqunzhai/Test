from gevent import monkey
import gevent
import time
from urllib.request import urlopen
monkey.patch_all()
#对比得出 协程 运行出的更快
#IO阻塞 自动切换任务。。
def say(url):
    print('get url',url)
    resp = urlopen(url)
    data = resp.read()
    print(len(data),url)
t1_start = time.time()
say('http://www.xiaohuar.com/')
say('http://www.oldboyedu.com/')
print("普通--time cost",time.time() - t1_start)

t2_stat = time.time()
gevent.joinall(
    [gevent.spawn(say,'http://www.xiaohuar.com/'),
     gevent.spawn(say,'http://www.oldboyedu.com/'),
     gevent.spawn(say,'http://weibo.com/MMbdzx?from=myfollow_all&is_all=1#_rnd1482040021384')]
)
print("gevent---time cost",time.time() - t2_stat)