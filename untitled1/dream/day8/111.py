# 一个进程下可以启动多个线程，多个线程共享父进程的内存空间，这也意味着
# 每个线程可以访问同一份数据，此时，如果2个线程同时要修改同一份数据，
# 会出现什么情况




import  time
import  threading

def AddNum():
    global  num  #在每个线程中都获取这个全局变量
    print("--get num:",num)
    time.sleep(2)
    num += 1  #对此公共变量进行+1操作

num = 10  #设置一个共享变量
threading_list = []
for i in range(10):
    t = threading.Thread(target=AddNum)
    t.start()
    threading_list.append(t)
for t in threading_list:
    t.join()

print("final num:",num)