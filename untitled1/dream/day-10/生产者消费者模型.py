import queue
import time
import threading

def consumer(name):
    while True:
        print('%s 取得蛋糕 %s并吃了它' %(name,q.get()))   #q.get 就是去队列中取值
        time.sleep(1)
        q.task_done()  #回执
        #每一个人在消费完这个任务之后，都要给你的生产者发送一个回执，生成站收集完所有的回执，就判断所有的任务是不是运行完，就可以结束了
def produce(name):
    count=0
    #while q.qsize() <5:  #因为队列设置的大小为4  那么这里设置小于5
    for i in range(10):
        print("%s生产了%s个蛋糕" %(name,count))
        q.put(count)
        count +=1
        #time.sleep(2)
    q.join()   #直到队列被消费完毕
    print('生产完了------')
q=queue.Queue(maxsize=4)
#创建线程
p1=threading.Thread(target=consumer,args=('rch',))
p2=threading.Thread(target=produce,args=('zcq',))
p3=threading.Thread(target=produce,args=('hahah',))
p1.start()
p2.start()
p3.start()