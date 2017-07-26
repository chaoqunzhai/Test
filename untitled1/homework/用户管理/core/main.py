#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from sqlalchemy import and_
import os,sys
BASEDIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASEDIR)
from database import Users,UserType,ZhuJi,UserToZhuji

engine = create_engine("mysql+pymysql://root:123456@192.168.1.10:3306/Dream", max_overflow=5)

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class ArvgHandler(object):

    def __init__(self):
        self.name = input("username:").strip()
        self.passwd = input("password:").strip()
        self.interactive()
    # def authenticate(self):
    #
    #     if self.get_auth_result(self.name,self.passwd):
    #         return True
    #     else:
    #
    #         retry_count = 0
    #         while retry_count < 2:
    #             username = input("username:").strip()
    #             password = input("password:").strip()
    #             if self.get_auth_result(username,password):
    #                 return True
    #             else:
    #                 retry_count += 1
    #                 continue
    #         else:
    #             exit("you have input wrong username or password 3 times")
    #
    # def get_auth_result(self,user,password):
    #     res = session.query(Users.name,Users.passwd).filter(and_(Users.name == user,Users.passwd == password)).all()
    #     if len(res)!= 0:
    #         print("Passed authentication")
    #         return True
    #
    #     else:
    #         print("username or password is wrong")
    #         return False

    def interactive(self):
        if True:
            print("欢迎来到菜狗子用户主机管理系统")
            msg = '''
            1.用户类型管理
            2.用户管理
            3.主机管理
            4.分配主机
            5.退出
            '''
            menu_dict ={
                '1':'Type',
                '2':'User',
                '3':'Zhuji',
                '4':'Relationship',
                '5':'exit'

            }
            while True:
                print(msg)
                choice = input(">>>").strip()
                if len(choice) == 0 or choice not in menu_dict:
                    continue
                elif choice == '5':
                    break
                else:
                    if hasattr(self,menu_dict[choice]):
                        func = getattr(self,menu_dict[choice])
                        func()
    def Type(self):
        msg = '''
        1.查看用户类型
        2.添加用户类型
        3.删除用户类型
        4.修改用户类型
        5.返回
        '''
        while True:
            print(msg)
            choice = input(">>>").strip()
            if choice == '1':
                res = session.query(UserType).all()
                session.commit()
                for i in res:
                    print(i)
            elif choice == '2':
                typename = input("你要添加的用户类型:").strip()
                obj = UserType(type=typename)
                session.add(obj)
                session.commit()
            elif choice == '3':
                typeid = input("你要删除的用户类型ID:").strip()
                session.query(UserType).filter(UserType.id == int(typeid)).delete()
                session.commit()
            elif choice == '4':
                typeid = input("你要修改的用户类型ID:").strip()
                option = input("你要修改的选项:").strip()
                typename = input("修改后的值:").strip()
                if option == 'id':
                    typename = int(typename)
                session.query(UserType).filter(UserType.id == int(typeid)).update({option:typename})
                session.commit()
            elif choice == '5':
                break

    def User(self):
        msg = '''
        1.查看用户信息
        2.添加用户
        3.删除用户
        4.更改用户信息
        5.返回
        '''
        while True:
            print(msg)
            choice = input(">>>").strip()
            if choice == '1':
                res = session.query(Users).join(UserType).all()
                session.commit()
                for i in res:
                    print("id:%s,name:%s,tid(typeid):%s" % (i.id,i.name,i.tid))
            elif choice == '2':
                name = input("username:").strip()
                passwd = input("password:").strip()
                id = input("tid:").strip()
                obj = Users(name=name,passwd=passwd,tid=int(id))
                session.add(obj)
                session.commit()
            elif choice == '3':
                id = input("你要删除的用户ID").strip()
                session.query(Users).filter(Users.id == int(id)).delete()
                session.commit()
            elif choice == '4':
                id = input("你要修改的用户ID:").strip()
                option = input("你要修改的选项:").strip()
                name = input("修改后的值:").strip()
                if option == "id":
                    name = int (name)
                session.query(Users).filter(Users.id == int(id)).update({option:name})
                session.commit()
            elif choice == '5':
                break

    def Zhuji(self):
        msg = '''
        1.查看主机信息
        2.添加主机
        3.删除主机
        4.修改主机信息
        5.返回
        '''
        while True:
            print(msg)
            choice = input(">>>").strip()
            if choice == '1':
                res = session.query(ZhuJi).all()
                session.commit()
                for i in res:
                    print(i)
            elif choice == '2':
                ip = input("你要添加的主机IP:").strip()
                port = input("连接该主机的端口为:").strip()
                obj = ZhuJi(ip=ip,port=port)
                session.add(obj)
                session.commit()
            elif choice == '3':
                id = input("你要删除的主机ID:").strip()
                session.query(ZhuJi).filter(ZhuJi.id == int(id)).delete()
                session.commit()
            elif choice == '4':
                id = input("你要修改的主机ID:").strip()
                option = input("你要修改的选项:").strip()
                name = input("修改后的值:").strip()
                if option == 'id' or option == 'port':
                    name = int(name)
                session.query(ZhuJi).filter(ZhuJi.id == int(id)).update({option:name})
                session.commit()
            elif choice == '5':
                break

    def Relationship(self):
        msg = '''
        1.查看用户主机关系
        2.添加用户主机关系
        3.删除用户主机关系
        4.返回
        '''
        while True:
            print(msg)
            choice = input(">>>").strip()
            if choice == '1':
                res = session.query(UserToZhuji).all()
                session.commit()
                for i in res:
                    print(i)
            elif choice == '2':
                user_id = input("要分配机器的用户ID:").strip()
                zhuji_id = input("被分配的主机ID:").strip()
                obj = UserToZhuji(user_id=int(user_id),zhuji_id=int(zhuji_id))
                session.add(obj)
                session.commit()
            elif choice == '3':
                id = input("你要删除的关系ID:").strip()
                session.query(UserToZhuji).filter(UserToZhuji.nid == int(id)).delete()
                session.commit()
            elif choice == '4':
                break













