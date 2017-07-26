import socket

client = socket.socket()

client.connect(('localhost',8070))


while True:
    msg = input('>>').strip()
    if len(msg) == 0 :continue
    client.send(msg.encode())#
    data = client.recv(1024)
    print('服务器给客户端返回的消息',data)