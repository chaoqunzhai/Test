from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import os
import sys

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

engine=create_engine('mysql+pymysql://root:123456@192.168.1.10:3306/Dream',max_overflow=5)

Base=declarative_base()

class Add_users(Base):
    __tablename__ = 'add_tables'
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(60))
    extra=Column(String(60))
class Users(Base):
    __tablename__='users' # 表名字叫users
    id=Column(Integer,primary_key=True,autoincrement=True)   #Integer整数, id为列, primart_key 主键，autoincrement自增
    name=Column(String(60),unique=True)     #name列,unique设置唯一
    passwd=Column(String(60),unique=True)   #extra列
    date = Column(String(100),unique=False)
    tid = Column(Integer, ForeignKey("user_type.nid"))
    usertype=relationship('User_Type',backref='user')
class User_Type(Base):
    __tablename__ = 'user_type'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    caption = Column(String(60),nullable=True,unique=True)
class Server(Base):
    __tablename__ = 'server'
    id = Column(Integer, primary_key=True,autoincrement=True)
    server_ip = Column(String(60), nullable=True,unique=True)
    server_port = Column(String(60),default=1314,nullable=True)  #nullable可空
class Servertoo(Base):
    __tablename__ = 'servertoo'
    nid = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey('users.id'))
    server_id = Column(Integer,ForeignKey('server.id'))
    users = relationship('Users',backref = 'a')
    server = relationship('Server',backref= 'b')
    def __repr__(self):
        temp="%s-%s-%s" %(self.nid,self.username,self.group_id)
        return temp
def init_db():
    Base.metadata.create_all(engine)
