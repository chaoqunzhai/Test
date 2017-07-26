import threading
def run(n):
    print('thring',n)

t_list=[]
for i in range(5):
    t=threading.Thread(target=run,args=(i,))
    t.start()
    t_list.append(t)       #执行完后的线程 加入到列表中 这样就能确保子线程就都执行万了
    #print(t_list)
for z in t_list:
    z.join()   #等待  join是主线程等待子线程执行完毕后，在执行
    #print('-',z)
print('我是主线程')