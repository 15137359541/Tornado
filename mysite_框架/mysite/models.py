"""
确定使用什么ORM操作
    pymysql?
    sqlalchemy? + pymysql
        pymysql.install_as_MySQLdb()

    > 目的：为了了解框架底层的东西，尝试自己开发一个完整的ORM操作模块，欢迎使用pymysql
    > 目的：为了项目[高效]开发，欢迎使用成熟的框架，如sqlalchemy
"""

from sqlalchemy import Column,String,Integer,create_engine,and_,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
pymysql.install_as_MySQLdb()
#构建一个基础类型：自定义所以的类型继承自该类型
BaseModel=declarative_base()
# 定义基础类模块

   #创建和数据库的连接引擎对象，通过引擎直接操作sql语句
engine = create_engine("mysql://root:root@localhost:3306/mytornado",
                           echo=True)




# 定义实体类
class User(BaseModel):
    # 创建和数据库的会话对象
    db_session = sessionmaker(bind=engine)

   #自定义类型和数据库中表的关联关系
    __tablename__="useres"
   #创建类型属性，同时关联数据库中表的字段
    id=Column(Integer,primary_key=True)
    name=Column(String(255))
    password=Column(String(255))
class Titles(BaseModel):
    db_session_title=sessionmaker(bind=engine)
    # 自定义类型和数据库中表的关联关系
    __tablename__ = "titles"
    # 创建类型属性，同时关联数据库中表的字段
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    contet = Column(Text)
    user=Column(Integer)
