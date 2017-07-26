from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import pymysql
Base = declarative_base()

class User(Base):
    __tablename__ = 'zcq'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32))
    extra = Column(String(16))



def init_db():
    engine = create_engine("mysql+pymysql://root:123456@192.168.73.100:3306/Dream?charset=utf8", max_overflow=5)
    Base.metadata.create_all(engine)

def drop_db():
    engine = create_engine("mysql+pymysql://root:123456@192.168.73.100:3306/Dream?charset=utf8", max_overflow=5)
    Base.metadata.drop_all(engine)

#init_db()

#
engine = create_engine("mysql+pymysql://root:123456@192.168.73.100:3306/Dream?charset=utf8", max_overflow=5)
Session=sessionmaker(bind=engine)

session=Session()

#添加一条信息
# obj1=User(id=1,name='root',extra='123456')
# session.add(obj1)



#添加多条
session.add_all([
    User(id=2,name='root2',extra='123456'),
    User(id=3,name='root',extra='123456')
])
session.commit()  #提交
#获取全部数据
v=session.query(User).all()
for rom in v:
    print(rom.id,rom.name,rom.extra)

q=session.query(User).first()
print(q.id,q.name,q.extra)

