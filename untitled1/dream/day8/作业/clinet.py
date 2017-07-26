#-*-:coding:utf-8-*-
import socket
import os
#E:\A-python视频\15期\day8\S15_Day8\S15_Day8\录制_2016_11_27_18_10_04_199.avi
class Client(object):
    conn_status = 0
    def __init__(self,name):
        self.name = name
    def file(self):
        afile='ClientDownload'
        if os.path.exists(afile) == False:
            os.mkdir('ClientDownload')
            os.chdir(afile)
            print('yes!!!')
        else:
            os.chdir(afile)
            print('存储目录已经存在')
        return afile
    def client(self):
        afile = Client.file(self)
        print(afile, os.getcwd())
        afile_data = afile + str(Client.conn_status)
        client = socket.socket()
        client.connect(('localhost',8003))
        with open(afile_data, 'wb') as f:
            while True:
                try:
                    while True:
                        chorice = input('client(put|get)>>').strip()
                        if len(chorice) == 0 :continue
                        client.send(chorice.encode())
                        data = client.recv(102400)
                        print(data)  #服务端回复的信息
                        if not data:break
                        if chorice == 'q':exit()
                        if len(chorice) == 0:break
                        if chorice == 'put':
                            chorice_put=input('\033[1;33m请输入绝对路径文件>>:\033[0m').strip()
                            try:
                                if os.path.exists(chorice_put):
                                    fileSize = os.path.getsize(chorice_put)
                                    print(fileSize)
                                    f=open(chorice_put,'rb')
                                    data = f.read()
                                    client.sendall(data)
                                else:
                                    print('do is file')
                            except PermissionError as q:
                                    print('\033[1;33m重新输入绝对路径\033[0m')
                        if chorice == 'get':
                            chorice_get = input('\033[1;33m请输入要下载的路径文件>>:\033[0m').strip()
                            f.write(data)
                            f.flush()
                except ConnectionAbortedError as e:
                    print('\033[1;32m您的操作过载\033[0m')
                except ConnectionResetError as f:
                    print('\033[1;32m关闭一个连接，重新打开一个连接\033[0m')
if __name__ == '__main__':
    a=Client('zcq')
    a.client()

