from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import and_
import os
import sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)


from conf import core


engine=create_engine('mysql+pymysql://root:123456@192.168.1.10:3306/Dream',max_overflow=5)

Base=declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
class ArvgHandler(object):
    def __init__(self):
        self.interactive()
    def interactive(self):
        print("---main ORM---")
        msg = '''
            1.用户类型管理
            2.用户管理
            3.主机管理
            4.退出
            5.增加表
            6.构造表
            '''
        msg_dict ={
                '1':'type',
                '2':'user',
                '3':'server',
                '4':'exit',
                '5':'add_table',
                '6':'handle'
            }
        while True:
            print(msg)
            choice = input(">>>").strip()
            if len(choice) == 0 or choice not in msg_dict:
                continue
            elif choice == '5':break
            else:
                if hasattr(self,msg_dict[choice]):
                    func = getattr(self,msg_dict[choice])
                    func()
    def type(self):
        msg = '''
        1.查看用户
        2.添加用户
        3.删除用户
        4.返回
        '''
        while True:
            print(msg)
            choice = input(">>>").strip()
            if choice == '1':
                res = session.query(core.User_Type).all()
                session.commit()
                for i in res:
                    print('--->nid为:%s,caption为:%s'%(i.nid,i.caption))
            elif choice == '2':
                typename = input("用户名称:").strip()
                obj = core.User_Type(caption=typename)
                session.add(obj)
                session.commit()
            elif choice == '3':
                nid = input("你要删除的用户NID:").strip()
                session.query(core.User_Type).filter(core.User_Type.nid == int(nid)).delete()
                session.commit()
            elif choice == '4':break
    def user(self):
        msg = '''
        1.查看用户信息
        2.添加用户
        3.删除用户
        4.返回
        '''
        while True:
            print(msg)
            msg_1 = '''
            1.列出表，
            2.根据用户名查询
            '''
            choice = input(">>>").strip()
            if choice == '1':
                print(msg_1)
                res = session.query(core.Users).join(core.User_Type).all()
                session.commit()
                for i in res:
                    print(i.id,i.name,i.tid)
                choice_1=input('>>>').strip()
                if choice_1 =='1':
                    cur = session.query(core.Users.id,core.Users.name.name,core.Users.passwd,core.User_Type.nid,core.User_Type.caption).all
                    print(cur)
            elif choice == '2':
                name = input("username:").strip()
                passwd = input("password:").strip()
                id = input("tid:").strip()
                obj = core.Users(name=name,passwd=passwd,tid=int(id))
                session.add(obj)
                session.commit()
                print('yes')
            elif choice == '3':
                id = input("你要删除的用户ID").strip()
                session.query(core.Users).filter(core.Users.id == int(id)).delete()
                session.commit()
                print('yes')
            elif choice == '4':break
    def server(self):
        msg = '''
        1.查看主机
        2.添加主机
        3.删除主机
        4.返回
        '''
        while True:
            print(msg)
            choice = input(">>>").strip()
            if choice == '1':
                res = session.query(core.Server).all()
                session.commit()
                for i in res:
                    print('ID为:%s，添加主机IP:%s，添加主机Port:%s'%(i.id,i.server_ip,i.server_port))
            elif choice == '2':
                ip = input("你要添加的主机IP:").strip()
                ports = input("连接该主机的端口为:").strip()
                obj = core.Server(server_ip=ip,server_port=ports)
                session.add(obj)
                session.commit()
            elif choice == '3':
                id = input("你要删除的主机ID:").strip()
                session.query(core.Server).filter(core.Server.id == int(id)).delete()
                session.commit()
            elif choice == '4':break
    def add_table(self):
        name=input('new table name>>:').strip()
        extras=input('extra>>:').strip
        obj=core.Add_users(name=name,extra=extras)
        session.add(obj)
        session.commit()
    def handle(self):
        core.init_db()
    def exit(self):
        exit()
if __name__ =='__main__':
    ArvgHandler()