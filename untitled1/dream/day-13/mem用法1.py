import memcache


conn=memcache.Client(['192.168.12.78:12000'],debug=True,cache_cas=True)

conn.set('zcq',900)
v=conn.get('zcq')
print(v)