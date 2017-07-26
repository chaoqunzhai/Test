from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import paramiko
import os,sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import setting
from conf import models


class SSH(object):
    def __init__(self):
        self.transport = None
    def close(self):
        self.transport.close()
    def cmd(self,cmd):
        ssh = paramiko.SSHClient()
        ssh._transport = self.transport
        stdin,stdout,stderr = ssh.exec_command(cmd)

        return stdout.read()
    def connect(self):
        try:
            self.transport = paramiko.Transport((setting.ip,setting.port))
            self.transport.connect(username=setting.user, password=setting.passwd)
        except Exception as e:exit('error---')
    def connect_windows(self):
        from bin import server
        server()
    def connect_mysql(self):
        tag = False
        while True:
            msg_2 = '''
            1:用户主机及密码管理
            2:堡垒机用户主机及密码管理
            3:exit
            '''
            msg_2_dict={
                '1':'open_user',
                '2':'open_admin',
                '3':'exit'
            }

            print(msg_2)
            choice3 = input('选择操作类型>>').strip()
            if choice3 =='1':
                if tag == False:
                    models.init_db()
                    tag=True
                else:
                    print('*******您已经操作数据库无需再建立')
            if len(choice3) == 0 or choice3 not in msg_2_dict:
                continue
            elif choice3 == '4':
                break
            else:
                if hasattr(self, msg_2_dict[choice3]):
                    func = getattr(self, msg_2_dict[choice3])
                    func()
    def open_user(self):
        while True:
            msg_3 = '''
                    a-1:查看用户和主机
                    a-2:增加用户名和管理主机
                    a-3:删除用户对应管理主机
                    b-1:查看用户
                    b-2:添加用户名及对应密码
                    b-3:删除用户名和密码
                    q:返回上级
                     '''
            print(msg_3)
            choice4 = input('添加用户>>').strip()
            if choice4 == 'a-1':
                res = models.session.query(models.Host).all()
                for i in res:
                    print('id为:%s，名称为:%s,管理主机为:%s' % (i.id,i.hostname, i.ip))
            elif choice4 == 'a-2':
                try:
                    name = input("用户名:").strip()
                    ip= input("管理主机IP:").strip()
                    id =input("远程端口:").strip()
                    obj=models.Host(hostname=name,ip=ip,port=int(id))
                    models.session.add(obj)
                    models.session.commit()
                    print('yes')
                except Exception as e:print('！用户名已经存在')
            elif choice4 == 'a-3':
                nid = input("你要删除的用户NID:").strip()
                models.session.query(models.Host).filter(models.Host.id == int(nid)).delete()
                models.session.commit()
            elif choice4 == 'b-1':
                ress=models.session.query(models.HostUser).all()
                for i in ress:
                    print('id为:%s，用户名:%s,密码:%s' % (i.id,i.username, i.password))
            elif choice4 == 'b-2':
                try:
                    usename = input("用户名:").strip()
                    passwd= input("密码:").strip()
                    cur=models.HostUser(username=usename,password=passwd)
                    models.session.add(cur)
                    models.session.commit()
                except Exception as e:print('！用户名已经存在')
            elif choice4 == 'b-3':
                hid=input("你要删除的用户ID:").strip()
                models.session.query(models.HostUser).filter(models.HostUser.id == int(hid)).delete()
                models.session.commit()
            elif choice4 == 'q':self.connect_mysql()
    def open_admin(self):
        while True:
            msg='''
            1:添加堡垒机用户,
            2:删除堡垒机用户
            3:查看堡垒机用户'
            4:返回上级
            '''
            print(msg)
            choice = input('添加堡垒机用户>>').strip()
            if choice == '1':
                try:
                    name=input("用户名>:").strip()
                    passwd=input("密码>:").strip()
                    obj=models.UserProfile(username=name,password=passwd)
                    models.session.add(obj)
                    models.session.commit()
                except Exception as e:print('！用户名已经存在')
            elif choice == '2':
                nid=input("你要删除的用户ID:").strip()
                models.session.query(models.UserProfile).filter(models.UserProfile.id == int(nid)).delete()
                models.session.commit()
            elif choice == '3':
                res = models.session.query(models.UserProfile).all()
                for i in res:
                    print('id为:%s，名称为:%s' % (i.id,i.username))
            elif choice == '4':self.connect_mysql()
    def interactive(self):
        msg='''
        1:后台管理(登录堡垒机级别)
        2:退出系统
        '''
        while True:
            print(msg)
            choice = input(">>>:").strip()
            if choice == '3':break
            if choice == '1':
                msg_1 = '''
                1:Windows方式连接堡垒机查看
                2:数据录入
                3:返回上级
                '''
                msg_dict ={
                    '1':'connect_windows',
                    '2':'connect_mysql',
                    '3':'exit',

                }
                while True:
                    print(msg_1)
                    choice1=input('>>:').strip()
                    if len(choice1) == 0 or choice1 not in msg_dict:
                        continue
                    elif choice == '4':
                        break
                    else:
                        if hasattr(self,msg_dict[choice1]):
                            func = getattr(self,msg_dict[choice1])
                            func()
    def exit(self):
        exit('baye--')
if __name__ == '__main__':
    obj=SSH()
    choic=input('命令测试是否连接成功（Y/N）:可以忽略>>').strip()
    if choic == 'Y':
        obj=SSH()
        obj.connect()
        choice2 = input('输入命令>>>:').strip()
        print(obj.cmd(choice2).decode())
        obj.close()
    else:
        obj.interactive()


