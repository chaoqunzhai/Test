import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('0.0.0.0',8070))

server.listen(5)
print('-----开始建立连接-----')
conn,client_addr = server.accept()
#conn 就是客户端连过来而在服务端为其生成一个连接实例
#print(conn,client_addr)     #打印连接信息
print('conn',conn)
print('client_addr',client_addr)
while True:
    data = conn.recv(1024)        #1024字节   接受套接字的数据，也就是接受客户端的套接字
    print('客户端给我发的消息',data)
    conn.send(b'got!!!!!')  # 将数据发送到连接的套接字  #放到缓冲区。缓冲区溢满 就发送。 为了优化网络传输效率  减少网络I/O     收一次应该不能超过10K