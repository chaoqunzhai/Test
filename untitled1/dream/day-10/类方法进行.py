import threading
import time


class Mythreading(threading.Thread):
    def __init__(self,runing):
        threading.Thread.__init__(self)
        self.runing = runing

    def run(self):  #这里定义的run方法
        print('定义每个线程要运行的函数%s' %self.runing)
        time.sleep(0.2)


if __name__ == '__main__':
    t1=Mythreading(1)
    t2=Mythreading(2)
    t1.start()
    t2.start()

print('----')
