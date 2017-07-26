from multiprocessing import Process,Queue
#这里的Queue是进程里面的队列 方法
def f(q):
    q.put([24,None,'zhaichaoqun'])



if __name__ == '__main__':
    q=Queue()
    p=Process(target=f,args=(q,))  #创建进程
    p.start()
    print(q.get())
    p.join()