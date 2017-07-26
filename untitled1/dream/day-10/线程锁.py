import threading
import time
def run(n):
    global  num
    I.acquire()  #获取锁
    num += 1
    time.sleep(1)
    I.release()  #释放锁
    print(num)
def run2():
    conunt = 0
    while num < 9:
        print('----',conunt)
        conunt +=1
I=threading.Lock()
num = 0
t_list = []
for i in range(10):
    t = threading.Thread(target=run, args=(i,))
    t.start()
    t_list.append(t)
t2=threading.Thread(target=run2)
t2.start()
for t in t_list:
    t.join()
print("--main thread---")
print(num)
