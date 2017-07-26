#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123456@192.168.1.10:3306/Dream", max_overflow=5)

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=True,unique=True)
    passwd = Column(String(50),nullable=True)
    tid = Column(Integer,ForeignKey("usertype.id"))
    usertype = relationship("UserType",backref='user')
    # def __repr__(self):
    #     return "%s.%s,%s" %s ()

class UserType(Base):
    __tablename__ = 'usertype'
    id = Column(Integer,primary_key=True,autoincrement=True)
    type = Column(String(50),nullable=True,unique=True)

    def __repr__(self):
        return "id:%s,type:%s" % (self.id,self.type)

class ZhuJi(Base):
    __tablename__ = 'zhuji'
    id = Column(Integer,primary_key=True,autoincrement=True)
    ip = Column(String(50),nullable=True,unique=True)
    port = Column(Integer,default=22,nullable=True)

    def __repr__(self):
        return "id:%s,ip:%s,port:%s" % (self.id,self.ip,self.port)

class UserToZhuji(Base):
    __tablename__ = 'usertozhuji'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    zhuji_id = Column(Integer,ForeignKey("zhuji.id"))
    users = relationship("Users",backref='u2z')
    zhuji = relationship("ZhuJi",backref='u2z')

    def __repr__(self):
        return "id:%s,user_id:%s,zhuji_id:%s" % (self.nid,self.user_id,self.zhuji_id)

def init_db():
    Base.metadata.create_all(engine)

#init_db()