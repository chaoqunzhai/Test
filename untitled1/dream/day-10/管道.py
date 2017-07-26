from multiprocessing import Process,Pipe

#管道
def f(conn):
    conn.send([42,None,'父亲'])
    conn.send([43,None,'word'])
    print('from parent',conn.recv())
    conn.close()


if __name__ == '__main__':
    parent_conn,child_conn = Pipe()       #管道 一个头一个尾  就好比 一个父亲 一个儿子
    p = Process(target=f,args=(child_conn,))  #定义是用来接受子请求
    p2 = Process(target=f, args=(child_conn,))
    p.start()
    p2.start()
    print(parent_conn.recv())     #打印 父去接受子的请求
    parent_conn.send('hellow 儿子')
    parent_conn.send('hellow 儿2子')
    p.join()
    p2.join()