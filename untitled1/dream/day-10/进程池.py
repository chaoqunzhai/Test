from  multiprocessing import Process, Pool,Lock
import time

def f(i):
    print('hello word %s' %i)
    time.sleep(1)
    return i
def callback(data):      #回执，相当于 子进程执行完毕后。告诉主进程.  这里callback还可以干很多事，因为这里设置的是把结果都返回给这里了。。所以可以把结果写入日志中
    print('exec done---->',data)

if  __name__ == '__main__':
    lock =Lock()

    pool = Pool(processes=5)  #设置线程池，有5个进程
    for num in range(100):
        pool.apply_async(func=f,args=(num,),callback=callback)

    pool.close()  #一定要close()   。告诉主进程说，进程池已经添加完毕，可以关闭了
    pool.join()  #进程池中进程执行完毕后在关闭。如果取消，那么程序直接就关闭了