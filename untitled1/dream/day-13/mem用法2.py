import memcache
import time

#这个先运行。等待5秒，然后运行mem用法1.py  才可出现
#如果正常会出错 MemCached: while expecting 'STORED', got unexpected response 'EXISTS'
#这是因为memcache的计步器...
#memcache算法。----
conn=memcache.Client(['192.168.12.78:12000'],debug=True,cache_cas=True)

v=conn.gets('zcq')
time.sleep(5)
conn.cas('zcq',666)