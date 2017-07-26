from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine,DateTime
from sqlalchemy_utils import ChoiceType



engine=create_engine('mysql+pymysql://root:123456@192.168.1.100:3306/Dream',max_overflow=5)
Base = declarative_base() #定义基类
Session = sessionmaker(bind=engine)
session = Session()

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer,primary_key=True,autoincrement=True)            #autoincrement自增,primary_key 外键
    hostname = Column(String(100),unique=True,nullable=False)  #unique唯一,nullable false 不能为空
    ip = Column(String(64),unique=True,nullable=False)
    port = Column(Integer,default=22)

    def __repr__(self):
        return self.hostname

class HostUser(Base):
    __tablename__ = 'host_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    # AuthTypes = [
    #     ('ssh-passwd','Password'),
    #     ('ssh-key','KEY'),
    # ]
    # #Authtypes里2个元组中的数据，第一个(ssh-passwd)是存在数据库中的，第二(SSH/Password)是是显示给我们看的，是映射关系
    # auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(100),unique=True,nullable=False)
    password = Column(String(100))

    host_id = Column(Integer,ForeignKey('host.id'))          #关联host表,添加时无需单加此条

    #唯一的约束
    __table_args = (
        UniqueConstraint('host.id','username',name='host_username_uc'),
    )
    def __repr__(self):
        return self.username

class UserProfile(Base):       #堡垒机用户名和密码
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(100),unique=True,nullable=False)
    password = Column(String(128),nullable=False)

    def __repr__(self):
        return self.username

class UserProfileUser(Base):          #堡垒机用户和主机的关系表
    __tablename__ = 'user_profile_host_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    host_user_id = Column(Integer,ForeignKey('host_user.id'))
    user_proflie_id = Column(Integer,ForeignKey('user_profile.id'))
    __table_args = (
        UniqueConstraint('user_profile.id','host_user.id',name='ux_user_host_user')
    )
class Auditlog(Base):
    __tablename__ = 'autid_log'
    id = Column(Integer,primary_key=True,autoincrement=True)

    cmd = Column(String(125))
    date = Column(DateTime)
    user_profile_id = Column(Integer,ForeignKey('user_profile.id'))
    host_user_id = Column(Integer,ForeignKey('host_user.id'))

def init_db():
    Base.metadata.create_all(engine)