import socket
import json
s = socket.socket()
#put C:\Users\Administrator\Desktop\无线.txt
s.bind(('localhost',9000))

s.listen(5)

while True:
    conn,client_addr = s.accept()
    print('go a new conn:',client_addr)

    while True:
        data = conn.recv(1024)
        print('recv:',data)
        data = json.loads(data.decode())

        if data.get('action') is not None:        #不是为空的意思
            print(data)
            if data['action'] == 'put':
                file_obj = open(data['filename'],'wb')
                receoved_size = 0
                while receoved_size < data['size']:
                    recv_data = conn.recv(4096)
                    file_obj.write(recv_data)
                    receoved_size += len(recv_data)
                    print(data['size'],receoved_size)
                else:
                    print('-----successfully-[%s]----'%(data['filename']))
                    file_obj.close()

            elif data['action'] == 'get':
                pass