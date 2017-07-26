import socket

client = socket.socket()

client.connect(('localhost',9000))

while True:
    choire = input(">>>").strip()
    if len(choire) == 0 :continue
    client.send(choire.encode())
    recv = client.recv(1024)
    print('recv:',recv.decode())