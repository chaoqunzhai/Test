import time
import datetime
print(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(time.time()) )
print(datetime.datetime.now())
print(time.strftime("%Y/%m/%d"))
print(datetime.datetime.now() + datetime.timedelta(3))

c_time  = datetime.datetime.now()
print(c_time.replace(minute=3,hour=2))

print(time.gmtime(time.time()))