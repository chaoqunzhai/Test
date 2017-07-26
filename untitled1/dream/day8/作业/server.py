#-*-:coding:utf-8-*-
import socket
import os
import sys
UPDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(UPDIR)

class Server(object):
    conn_status = 0
    def __init__(self,name):
        self.name = name
    def file(self):
        afile='ServerDownload'
        if os.path.exists(afile) == False:
            os.mkdir('ServerDownload')
            os.chdir(afile)
            print('yes!!!')
        else:
            os.chdir(afile)
            print('存储目录已经存在')
        return afile
    def server(self):
        afile=Server.file(self)
        print(afile,os.getcwd())
        afile_data = afile + str(Server.conn_status)
        with open(afile_data, 'wb') as f:           #只能传输一次文件，如果要传输2个文件要打开2个客户端
            while True:
                server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server.bind(('localhost',8003))
                server.listen(5)
                print('\033[1;33m---开始建立连接--\033[0m')
                conn, addr = server.accept()
                print('状态信息:', conn, addr)
                try:
                    while True:
                        data = conn.recv(10240000)
                        print('\033[1;33mclient操作>>\033[0m', data)
                        if not data:continue
                        conn.send(b'my is Server!')
                        Server.conn_status += 1
                        if Server.conn_status > 10:break
                        if len(data) > 10 :
                            f.write(data)
                            f.flush()
                        elif data.decode() == 'get':
                            print('\033[1;31m客户端下载模式\033[0m')
                            print(data.decode())
                        else:
                            print(len(data))
                            print(data)
                            print('\033[1;32m内容值太少，不值得写入存储\033[0m')
                        server.close()
                except ConnectionResetError as e:
                        print('\033[1;32m对方中断了连接\033[0m')
if __name__ == '__main__':
     a=Server('zcq')
     a.server()
