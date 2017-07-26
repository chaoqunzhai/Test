import select
import socket
import queue
server = socket.socket()
server.bind(('localhost',9999))
server.listen(5)
server.setblocking(False)  #设置为非阻塞

inputs=[server]  #交给select管理
msg_queuses={}
outputs=[]

while True:
     r_list,w_list,exception_list=select.select(inputs,outputs,inputs)  #select来管理
     #内核返回给select是一个完整的列表  假如你有500个连接,就给你返回500个，但是select帮我们处理了 把这500个里面有几个就绪的在过滤出来
     #返回给我的用户程序就是  r_list,w_list,exception_list
     #所以此时用户程序再去循环这个r_list的时候，看到的就已经是就绪的了！！！
     #r_list只要有返回，就肯定是有数据的！ select已经帮你过滤好了

     for s in r_list:
         if s in server:
             conn,addr = s.accept()
             print('客户端的信息',conn,addr)

             inputs.append(conn)    #把用户发过来的数据加入到select处理中  因为上面已经写了个select方法直接添加即可

             msg_queuses[conn] = queue.Queue()  #以conn为key 生成一个队列
         else:
             try:
                 data = s.recv(1024)
                 print("recv data from [%s]:[%s]" %(s.getpeername(),data.decode()))
                 msg_queuses[s].put(data)
                 if s not in outputs:
                    outputs.remove(s)
             except ConnectionResetError as e:
                 print("conn closed ",s.getpeername(),e)

                 inputs.remove(s)
                 if s in outputs:
                     outputs.remove(s)
                 del msg_queuses[s]

     for s in w_list:
         try:
             data = msg_queuses[s].get_nowait()
             s.send(data.upper())
         except queue.Empty as e:
             outputs.remove(s)