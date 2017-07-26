import time
import paramiko
import configparser
import os
import sys
import optparse
from multiprocessing import Process,Pool,Lock

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import settings

tag = False
date=time.strftime('%Y%m%d%M%S')
class Handler(object):
    def __init__(self):
        parser = optparse.OptionParser()
        parser.add_option("-s",'--host',dest='host',help='请输入主机IP地址')
        parser.add_option("-t",'--item',dest='item',help='请输入用户组')
        parser.add_option("-c", "--cmd", dest="cmd", help="请输入linux命令")
        parser.add_option("-u", "--username", dest="username", help="请输入用户名")
        parser.add_option("-P", "--password", dest="password", help="请输入密码")
        parser.add_option("-g", "--group", dest="group", help="请输入HOST组")
        parser.add_option("-f", "--courese", type='int',dest="courese", help="指定进程数")
        self.options,self.args =parser.parse_args()   #这里option是一个对象,保存命令行参数值，option.host 就可以访问值 args返回一个位置参数
        # self.auth()
        #self.conn()
    def configs(self):
        config = configparser.ConfigParser()
        config.read(settings.DB_DIR)
        return config
    def configroups(self):
        configs = configparser.ConfigParser()
        configs.read(settings.HOSTS_DIR)
        return configs
    def auth(self):
        respon=self.configs()
        if len(self.args) == 3:
            return False
       # print(config.sections())
        #serct= config[options.group]
        print('cmd------',self.options.cmd)
        if self.options.item in respon.sections():
            #print(config[options.group])
            #print(respon[self.options.item]['user'],respon[self.options.item]['password'])
            anuser='admin'
            anpassword='admin'
            if self.options.username == anuser and self.options.password == anpassword:           #in respon.sections():
                for i in respon[self.options.item]:
                    print('项目%s，内容%s' %(i,respon[self.options.item][i]))
                global tag
                tag = True
                return True
            else:
                print('密码or用户名错误--')
                exit()
    def conn(self):
        #self.acquire()
        respon = self.configs()   #db 用户文件
        respons = self.configroups()   #host ip 文件
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if self.options.group in respons.sections():          #指定-g参数执行
            print('--配置文件组--- %s     --hosts %s' %(respon.sections(),respons.sections()))
            if tag == True:        #远程程序密码通过了 才会去读取db文件内的用户名和密码
                for i in respons[self.options.group]:
                    print('管理IP节点为:%s '%i)
                   # print('tag yes ') 测试tag
                    print('操作用户:%s，密码:%s' %(respon[self.options.item]['user'], respon[self.options.item]['password']))
                    print('-------------------host主机地址%s-------------------' %(respons[self.options.group][i]))  #去检测hosts文件内的主机
                    try:
                        #if respon[self.options.item]['password'] in
                        ssh.connect(hostname=respons[self.options.group][i], port=22, username=respon[self.options.item]['user'],
                                    password=respon[self.options.item]['password'])
                        stdin, stdout, stderr = ssh.exec_command(self.options.cmd)
                        result = stdout.read(102400)
                        print('-------------------%s结果------------------' %self.options.cmd)
                        print(result.decode())
                        print('-------------------end------------------')
                        print(stderr.read().decode())
                       # print(stdin.read().decode())
                    except Exception as e:
                        print('如需要远程命令操作--请输入命令参数')
        elif self.options.group not in respons.sections():      #不采用-g参数执行
            print('<<不采取group组 单IP>>')
            if self.options.host:
                if respon[self.options.item]['host'] == self.options.host:      #获取参数值中的host和db文件中的host做对比。   我的角度是防止出错，用户和IP不对应
                    try:
                        ssh.connect(hostname=self.options.host, port=22, username=respon[self.options.item]['user'],
                                    password=respon[self.options.item]['password'])

                        stdin, stdout, stderr = ssh.exec_command(self.options.cmd)
                        result = stdout.read(102400)
                        print(result.decode())
                        print(stderr.read().decode())
                    except Exception as q:
                        print('如需要远程命令操作--请输入命令参数')
                else:
                    print('VIP用户对应的管理IP不对应')
            else:
                print('输入的IP地址参数')
    def callback(self):
        print('callback----',self)
    def interactive(self):
        if self.auth():     #执行auth函数
             print('---命令输入成功,-good!!')
             self.conn()
             print(' 父进程pid：%s，子进程pid：%s,时间为%s' % (os.getppid(), os.getpid(),date))
        else:
            print('请加 -h 查看命令参数,核对好信息')
    def run(self):
        lock = Lock()
        #self.interactive()
        pool = Pool(processes=4)
        if self.options.courese:
            if self.options.courese< 4:
                #for num in self.options.courese:
                #print(self.options.courese,type(self.options.courese))
                for i in range(self.options.courese):
                    #i.acquice()
                    pool.apply_async(func=self.interactive,callback=callable)
                    #i.release()
                pool.close()
                pool.join()
            else:print('....big coures..')

        else:self.interactive()

if __name__ == '__main__':
    t=Handler()
   # t.interactive()
    t.run()