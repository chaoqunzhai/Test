import threading
import time

#线程宏观上看起来是并行的
def run(n):
    time.sleep(0.2)
    print("threading",n)
#print('------')     #主线程
for i in range(5):           #创建子线程  如果子线程下又有子线程。 那这个线程死掉后。其子线程不会死掉  但是 程序的主线程死掉， 就是程序执行关闭了  其下面的子线
    t = threading.Thread(target=run, args=(1993,))
    t.start()
    #t.join()
    t.setName('t--%s' %i)    #修改线程名称
    #print(t.getName())          #获取线程名

print(threading.active_count())
print('我是主线程')       #主线程先执行  虽然看起来是主线程最后执行。实际上  不是。 那是因为 线程执行很快  打印显示出子线程就出来了

# t = threading.Thread(target=run,args=(1993,))
# t.start()
# print('------')
# t2 = threading.Thread(target=run,args=(1994,))
# t2.start()