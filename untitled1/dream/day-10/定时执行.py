import threading
#在线程里等三秒。和等三秒执行线程的区别
def hello():
    print('hello word')

t=threading.Timer(3.0,hello)
t.start()

print('----')