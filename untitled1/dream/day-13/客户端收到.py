
import redis

conn=redis.Redis(host='192.168.12.48')

pub = conn.pubsub()

pub.subscribe('zcq')

while True:
    msg = pub.parse_response()
    a=str(msg)
    print(a.encode('gbk'))