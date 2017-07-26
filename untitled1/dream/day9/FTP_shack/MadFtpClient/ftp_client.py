#-*- coding: utf-8 -*-
import socket
import os
import json
import optparse
import hashlib


STATUS_CODE = {
    400:'Invalid cmd format',
    401:'Invalid cmd',
    403:'Invalid auth data',
    600:'Wrong username or password',
    601:'Passed authentication',
    602:'Not filename',
    603:'File does is server',
    604:'read good!',
    605:'md5 varification',
	606:'filename put..',
    607:'all filename'
}

class FTPClient(object):
    def __init__(self):
        parser = optparse.OptionParser()          #这里模块就是来得到命令行参数
        parser.add_option("-s","--server",dest="server",help="输入服务端IP地址")      #使用add_option来定义命令行参数
        parser.add_option("-P", "--port", type='int',dest="port", help="输入服务端端口")      #这里可以限制type类型。
        parser.add_option("-u", "--username", dest="username", help="输入用户名")
        parser.add_option("-p", "--password", dest="password", help="输入密码")
        self.options,self.args =parser.parse_args()  #调用parse_args() 来解释程序命令行

        self.verify_args(self.options,self.args)
        self.make_connection()  #定义函数 跟远程去连接


    def make_connection(self):        #建立连接
        try:
            self.sock = socket.socket()
            self.sock.connect((self.options.server,self.options.port))         #这里面的值 也是去读取上面__init__中 add添加的值
        except TypeError as e:
            exit('-后面必须跟参数 -h 可查看')
    def verify_args(self,options,args):       #校验参数合法性，也就是检测命令行输入规则
        if options.username is not None and options.password is not None:
            pass
        elif options.username is None and options.password is None:
            pass
        else:
            exit('error!')
        if options.server and options.port:     #这个地方就是上面paser.add_option配置的地方
            #print(options)  打印你的命令参数值打印结果为:{'port': 1024, 'username': 'cq', 'password': 'cq', 'server': 'localhost'}
            if options.port >0 and options.port < 65535:
                return  True
            else:
                exit('没有那么大的端口。。。')
    def authenticate(self):  #用户验证
        if self.options.username:
            #print(self.options.username,self.options.password)  打印option 定义的命令行参数
            return self.get_auth_result(self.options.username,self.options.password)      #因为下面interactive会调用这里

        else:
            num = 0
            while num <3:
                username = input("username:(cq)>>").strip()
                password = input("password:(123)>>").strip()
                return self.get_auth_result(username,password)         #因为下面interactive会调用这里

    def get_auth_result(self,user,password):  #跟远程去交涉  这里就是给服务段传过去 服务端对这段字典，进行判断，来给客户端返回状态码
        data = {'action':'auth',
                'username':user,
                'password':password}
        self.sock.send(json.dumps(data).encode())   #发送上诉定义的data内容给服务端
        response = self.get_response()
        if response.get('status_code') == 601:        #这步操作就是去判断服务端send过来的数据
            print('Passwd authentication！')
            self.user = user
            return True
        else:
            print(response.get('status_msg'))
        print("response:",data)
    def get_response(self):       #这里就是函数就是定义 客户端给服务器发出的指令是否合法.   也是服务器给客户端返回的状态码，统一进行判断 很多地方调这里
        data = self.sock.recv(1024)
        data = json.loads(data.decode())   #loads方式读取服务端发过来的dumps数据
        return data
    '''
    def send_response(self,status_code,data=None):
        #data = self.sock.recv(1024)
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:
            response.update(data)
        self.sock.send(json.dumps(response).encode())
        return data
    '''
    def interactive(self):
        if self.authenticate():
            print('---用户通过认证----')
            while True:
                choice = input("%s:" %self.user).strip()
                if len(choice) == 0:continue
                if choice == 'q':exit('bay')
                cmd_list = choice.split()       #用户输入的值
                if hasattr(self,"_%s" %cmd_list[0]):    #反射  得到这个字符串 然后调用
                    func = getattr(self,"_%s"%cmd_list[0])
                    func(cmd_list)      #这里就是反射调用
                else:
                    print('命令格式错误')

    def __md5_required(self,cmd_list):  #用来检测是否需要md5
        if '--md5'in cmd_list:       #如果用户命令行参数有--md5 这个值 就调用定义的md5函数
            return True
    def show_progress(self,total):
        received_size = 0
        current_percent = 0
        while received_size < total:
             if int((received_size / total) * 100 )   > current_percent :
                  print("#",end="",flush=True)
                  current_percent = int((received_size / total) * 100 )
             new_size = yield
             received_size += new_size

    def _ls(self,cmd_list):
        print("__ls",cmd_list)
        if len(cmd_list) == 1:
            return False
        data_header = {
            'action':'ls',
            'type':607,
            'user':self.user
        }
        if len(cmd_list) == 1:
            return False
        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print('服务端发过数据',response)
        if response['status_code'] == 610:
            self.sock.send(b'1024')
            data = self.sock.recv(1024)
            print('当前目录文件',data.decode('utf-8'))
            #print(type(data))
            print(type(eval(data)))
            data_dict=eval(data)
            print('[%s] 家目录文件如下 \n<---%s--->'%(self.user,data_dict['file_all']))
    def _put(self,cmd_list):
        print("__put", cmd_list)
        if len(cmd_list) == 1:
            return False
        if os.path.isfile(cmd_list[1]):
            file_size = os.path.getsize(cmd_list[1])
            filename = cmd_list[1].split('/')[-1]
            data_header = {
                'action':'put',
                'filename':filename,
                'filesize':file_size
            }
            if self.__md5_required(cmd_list):
                data_header['md5'] = True

            self.sock.send(json.dumps(data_header).encode())
            self.sock.recv(1024)
            response = self.get_response()
            print('服务端发过数据', response)
            if self.__md5_required(cmd_list):
                md5_obj = hashlib.md5()
                progress = self.show_progress(data_header['filesize'])  # generator
                progress.__next__()
                with open(cmd_list[1],'rb') as file_obj:
                    for line in file_obj:
                        self.sock.send(line)
                        try:
                            progress.send(len(line))
                        except StopIteration as e:
                            print("-----100%")
                        md5_obj.update(line)
                    else:
                        md5_val = md5_obj.hexdigest()
                        self.get_response()
                        self.sock.send(json.dumps({'md5': md5_val}).encode())
                        print("上次完毕....")
                        md5_from_server=self.get_response()
                        if md5_from_server['status_code']==605:
                            print("%s 文件一致性校验成功!" % cmd_list[1])
            else:
                progress = self.show_progress(data_header['filesize'])
                progress.__next__()
                with open(cmd_list[1],'rb') as file_obj:
                    for line in file_obj:
                        self.sock.send(line)
                        try:
                            progress.send(len(line))
                        except StopIteration as e:
                            print("100%")
                print("上传完毕")
    def _get(self,cmd_list):
        print("_get,",cmd_list)
        if len(cmd_list) == 1:
            return False
        #if os.path.isfile(cmd_list[1]):
        #发送data_header信息
        data_header = {
            'action':'get',
            'filename':cmd_list[1]            #文件
        }
        if self.__md5_required(cmd_list):       #在data_header字典中增加这个key:value
            data_header['md5'] = True

        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print('服务端发过数据',response)
        if response['status_code'] == 604:
           # print('1111',cmd_list)  这里就是切片得到用户输入要下载的的文件名称
            self.sock.send(b'1')
            base_filename = cmd_list[1].split('/')[-1]   #切分并取最后一个值

            received_size = 0
            file_obj = open(base_filename,'wb')
            if self.__md5_required(cmd_list):     #如果服务端传过来的数据 带有md5 的key
                md5_obj = hashlib.md5()
                progress = self.show_progress(response['file_size']) #generator
                progress.__next__()
                while received_size < response['file_size']:   #response 这里是通过服务端返回的状态得到大小
                    data = self.sock.recv(4096)   #建立socke连接 连接为4096
                    received_size +=len(data)       #每次循环得到data的行数，并相加 赋值给received_size  。这里while循环，直到这个行数大于response的valve值
                    try:
                      progress.send(len(data))
                    except StopIteration as e:
                      print("100%")
                    file_obj.write(data)
                    md5_obj.update(data)         #
                else:
                    print('--->>接受完毕---')
                    file_obj.close()
                    md5_val = md5_obj.hexdigest()     #客户端对收到的数据进行md5 计算
                    #self.get_response()        #收服务端的数据  其中带有了md5的值
                    md5_from_server = self.get_response()
                    if md5_from_server['status_code'] == 605:  #从服务端返回的数据中去搜索这个值是否为605
                        if md5_from_server['md5'] == md5_val:
                            print("文件一致性校验成功！",base_filename)
                    print(md5_val,md5_from_server)
            else:  #如果没有md5的值
                progress = self.show_progress(response['file_size']) #generator
                progress.__next__()
                while received_size < response['file_size']:  # response 这里是通过服务端返回的状态得到大小
                    data = self.sock.recv(4096)  # 建立socke连接 连接为4096
                    received_size += len(data)  # 每次循环得到data的行数，并相加 赋值给received_size  。这里while循环，直到这个行数大于response的valve值
                    file_obj.write(data)
                    try:
                      progress.send(len(data))
                    except StopIteration as e:
                      print("100%")
                else:
                    print('--->>接受完毕---')
                    #file_obj.close()
    def _pwd(self,cmd_list):
        print('_pwd',cmd_list)
        #file_home_path=user_home_dir.split('/')[-1]
        #print(file_home_path)
        if len(cmd_list) == 1:
            return False
        data_header = {
            'action':'pwd',
            'user':self.user
        }
        self.sock.send(json.dumps(data_header).encode())
        response = self.get_response()
        print('服务端发过数据', response)
        #print(type(response))
        if response['status_code'] == 611:
            self.sock.send(b'1')
            print('您的家目录是/%s'%response['file_all'])

if __name__ == "__main__":
    ftp =FTPClient()
    ftp.interactive()