
import socketserver
import json
import configparser
from conf import settings
import os
import hashlib


#设置的常量
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
    610:'filename all',
    611:'pwd....'
}

class FTPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            print(self.client_address[0])
            print(self.data)
            print('远程主机强迫关闭了一个现有的连接')
            if not self.data:break
            #self.request.sendall(self.data.upper())     #给客户端返回
            data = json.loads(self.data.decode())
            if data.get('action') is not None:  #不是为空的
                if hasattr(self,'_%s'%data.get('action')):
                    func = getattr(self,'_%s'%data.get('action'))
                    func(data)         #get到action的value 并调用 如调用auth函数
                else:
                    #无效的命令，获取不到action这个key
                    self.send_response(401)
            else:
                #格式错误   下面已经封装好了这个函数用法
                self.send_response(400)
    def send_response(self,status_code,data=None):   #公用函数 很多地方调用
        '''  给客户端返回数据
        这里的意思是 得到客户端发送过来的data字典，并给字典中新增一个数据， STATUS_CODE上定义了状态码，
        上层handle中，根据用户输入状态 来调用这个函数，并把这个函数的结果增加到字典中，发送给客户端，客户端
        那边对这个状态码进行分析
        '''
        response = {'status_code':status_code,'status_msg':STATUS_CODE[status_code]}
        if data:      #这里data 定义了必须是字典 如果data存在就更新
            response.update(data)  #更新添加 客户端传过来的字典
        self.request.send(json.dumps(response).encode())     #如果data不存在，就把这个状态码返回给客户端

    def _auth(self,*args,**kwargs):
        #print("--auth",args,kwargs)
        data = args[0]       #args[0]就是整个 客户端传过来的字典
        if data.get("username") is None or data.get("password") is None:
            self.send_response(403)
        user = self.authenticate(data.get("username"),data.get("password"))
        if user is None:
            self.send_response(600)
        else:
            print('用户信息>:',user)
            self.user = user
            self.send_response(601)



    def authenticate(self,username,password): #这里是验证用户合法性，合法就返回用户数据
        config = configparser.ConfigParser()
        config.read(settings.ACCOUNT_FILE)
        if username in config.sections():           #是否用户名在这个文件中
            _password = config[username]["Password"]       #去取文件中的值 来进行判断密码
            if _password == password:
                print('pass auth....',username)
                config[username]["Username"] = username    ##应该是username 的赋值
                return config[username]
            else:
                return False
        else:
            return False
    def _put(self,*args,**kwargs):
        "client send file to server"
        data=args[0]
        if data.get('filename') is None:
            self.send_response(502)
        user_home_dir = "%s/%s" %(settings.USER_HOME,self.user["Username"])
        file_abs_path = "%s/%s" %(user_home_dir,data.get('filename'))
        print("file abs path",file_abs_path)

        self.request.send(b'1')
        resive_size=0
        print(data)
        if data.get('md5'):
            md5_obj = hashlib.md5()
            with open(file_abs_path,'wb') as file_obj:
                while data['filesize'] > resive_size:
                    line = self.request.recv(1024)
                    resive_size += len(line)
                    file_obj.write(line)
                    md5_obj.update(line)
                    #print(resive_size,len(line))
            self.request.send(b'1')
            respone=self.request.recv(1024)
            md5_val=json.loads(respone.decode())['md5']
            print('md5_val',md5_val)
            if md5_obj.hexdigest() ==md5_val:
                self.send_response(605)
            print("file [%s] 传输完毕---."%data.get('filename'))
        else:
            with open(file_abs_path,'wb') as file_obj:
                while resive_size < data['filesize']:
                    line = self.request.recv(1024)
                    resive_size += len(line)
                    print(resive_size,len(line))
                    file_obj.write(line)
            print("file [%s] 传输完毕---."%data.get('filename'))

    def _get(self,*args,**kwargs):
        data = args[0]  #数据本身
        if data.get('filename') is None:
            self.send_response(602)
        user_home_dir = "%s/%s" %(settings.USER_HOME ,self.user["Username"])  #这里是引用setting中配置的目录 和用户目录拼接
        file_abs_path = "%s/%s" %(user_home_dir,data.get('filename'))   #这里是get 客户端返回的信息  然后拼接目录
        print("file path",file_abs_path)
        if os.path.isfile(file_abs_path):
            print('---文件存在---')
            file_obj = open(file_abs_path,'rb')
            file_size = os.path.getsize(file_abs_path)
            self.send_response(604,data={'file_size':file_size})    #给客户端返回状态信息。并返回文件大小
            self.request.recv(1)     #阻塞客户端请求 解决黏包问题
            if data.get('md5'):  # 去get  ，客户端返回的数据中是否有md5这个值
                md5_obj = hashlib.md5()
                #这里用for循环，边读边写发送给客户端
                for line in file_obj:
                    self.request.send(line)
                    md5_obj.update(line)
                else:
                    #file_obj.close()
                    print('-->md5--',md5_obj.hexdigest())
                    md5_val = md5_obj.hexdigest()
                    self.send_response(605,{'md5':md5_val})
                    print('--->传输完毕---')
                    print(data)
            else:
                for line in file_obj:
                    self.request.send(line)
                else:
                    file_obj.close()
                    print('--->传输完毕---')
        else:
            self.send_response(603)
    def _ls(self,*args,**kwargs):
        print('_ls')
        data = args[0]
        user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
        print(user_home_dir)
        self.send_response(610)
        self.request.recv(1)
        if data.get('type'):
            os.chdir(user_home_dir)
            file_name_all = os.listdir()
            print(type(file_name_all))
            #for line in file_name_all:
            #    print(line)
            self.send_response(610, data={'file_all': file_name_all})
            #self.send_response(file_name_all)
            self.request.recv(1024)
        else:
            print('error----')
    def _cd(self,*args,**kwargs):
        pass
    def _pwd(self,*args,**kwargs):
        print('_pwd')
        data = args[0]
        if data.get('user'):
            user_home_dir = "%s/%s" % (settings.USER_HOME, self.user["Username"])
            print(user_home_dir)
            file_path =user_home_dir.split('/')[-2]
            print('/%s'%file_path)
            self.send_response(611, data={'file_all': file_path})
            self.request.recv(1024)
            #self.request.send(b'file_path')
        else:
            print('error----')


    def _mkdir(self,*args,**kwargs):
        print('_mkdir')

if __name__ == "__main__":
    HOST,PROT = "localhost",9999