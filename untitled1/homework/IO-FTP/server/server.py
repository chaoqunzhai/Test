import socket
import selectors
import json
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
DB_HOME = '%s\server\DB' %BASE_DIR
#C:\Users\Administrator\Desktop\ceshi.avi
class Server(object):
#sel = selectors.DefaultSelector() #实例一个sel
    def __init__(self):
        self.sel = selectors.DefaultSelector()
        self.respon()
    def accept(self,server,mask):
        conn,addr = server.accept()
        print('conn:%s from:%s' %(conn,addr))
        conn.setblocking(False)
        self.sel.register(conn,selectors.EVENT_READ,self.read)   #新连接来了注册一个事件,并调用read方法
    def respon(self):
        self.server = socket.socket()
        self.server.bind(('localhost',9000))
        self.server.listen(10)
        self.server.setblocking(False)  #设置为非阻塞

        self.sel.register(self.server,selectors.EVENT_READ,self.accept)  #把sock注册到sel实例中，注册一个为读事件,如果有请求过来就调用accept函数(可以自己定义一个函数)
#这句等同于  r_list,w_list,exception_list=select.select(inputs,outputs,inputs)
        #print('server------',self.server)
        while True:
            self.events = self.sel.select()  #开始监听事物，如果没有就卡主了
            for key, mask in self.events:
                callback = key.data  #accept       回调函数
                print('mask:',key,mask)
                print('fileobj:',key.fileobj)  #key.fileobj就相当于slef.server
                callback(key.fileobj, mask)
            #return key.fileobj
    def read(self,conn,mask):
        try:
            data = conn.recv(4096)
            if data:
                print('echoing to %s ' %conn)
                #conn.send(data)
                data = json.loads(data.decode())
                #data=data.decode()
                print(data)
                try:
                    if data.get('action') is not None:
                        if hasattr(self, '_%s' % data.get('action')):
                            func = getattr(self, '_%s' % data.get('action'))
                            #self.sel.register(conn, selectors.EVENT_READ, self.read)
                            func(conn,mask,data)  # get到action的value 并调用 如调用auth函数
                    else:print('error')
                except AttributeError as e:  #笨方法处理。。
                    pass
            else:      #如果没有消息就取消注册
                self.sel.unregister(conn)
                conn.close()
        except ConnectionResetError as e:
            print('client is down ')
            exit()
        # def put(*args):
        #     print('-------')
    def _put(self,conn,mask,*args):
        #print('-----------')
        os.chdir(DB_HOME)
        data=args[0]
        print('conn',conn)
        print('_put data',args[0])
        recvsize = 0
        conn.setblocking(False)
       # conn.recv(1024)
        if data.get('filename') is not None:
            filename = data.get('filename')
            filesize = data.get('filesize')
            print('filename',filename)
            with open(filename,'wb') as file:
                #self.server.recv(4096)
               # data = conn.recv(4096)
                print('recv----')
                while filesize > recvsize:
                   # line= self.server.recv(1024).decode()
                    try:
                        line = conn.recv(1024)
                        recvsize += len(line)
                        file.write(line)
                        file.flush()
                    except BlockingIOError as f:pass
                #print('yes')
    def _get(self,conn,mask,*args):
        print('_get data',args[0])
        data = args[0]
        # print('conn',conn)
        # print('mask', mask)
        if data.get('filename') is not None:
            filename = data.get('filename')
           # print(filename)
            DB_GET='%s/%s' %(DB_HOME,filename)
            print(DB_GET)
            for key, mask in self.events:  # 调用上面的这个events方法来得到类似于socket实例后的参数
                print('get-----', key, mask)
                print('----')
                print('fileobj:', key.fileobj)
          #  key.fileobj.send(b'1')
            if os.path.isfile(DB_GET):
                file_obj = open(DB_GET,'rb')
                file_size = os.path.getsize(DB_GET)
                print('go in db host')
                for line in file_obj:
                    key.fileobj.send(line)
              #  self.server.send(b'11')
               # for line in file_obj:


if __name__ == '__main__':
    a=Server()
    a.respon()


