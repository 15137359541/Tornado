"""
定义数据模型的管理器对象
"""
from . import models


class BaseManager(object):
    """
    对于数据对象的增删改查操作的基础类型
    """
    session=models.User.db_session()




class UserManager(BaseManager):
    """
    用户管理类型 ，继承自BaseManager

    """
    def __init__(self,id,name,password):
        self.id=id
        self.name=name
        self.password=password
    def create_obj(self):
        #创建一个模型对象
        user=models.User(id=self.id,name=self.name,password=self.password)
        #增加对象数据到数据库
        self.session.add(user)
        #提交事务
        self.session.commit()

    def update_obj(self):
        pass

    def delete_obj(self):
        pass

    def find_single(self):
        user=self.session.query(models.User).filter_by(name=self.name,
                                                  password=self.password).one()
        return user
    def find_multi(self):
        pass
