import threading,time

def run(n):
    time.sleep(1)
    print('threading',n)

for i in range(10):
    t=threading.Thread(target=run,args=(1,))
    t.setDaemon(True)       #主线程执行完毕后。子线程也就不执行了。。   这里是设置子线程为主线程的守护线程
    t.start()

print('-------')