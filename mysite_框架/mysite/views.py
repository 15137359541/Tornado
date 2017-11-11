'''
视图处理
'''
import simplejson as json
import tornado.web
from . import models_manage
class BaseHandler(tornado.web.RequestHandler):
    '''所有视图类的基础类
    '''
    def get_current_user(self):
        user=self.get_secure_cookie("login")
        if user:
            return True
        else:
            return False

class IndexHandler(BaseHandler):
    #首页必须登录才能访问
    # @tornado.web.authenticated
    def get(self):
        self.render("index.html")

class LoginHandler(BaseHandler):
    def get(self):
        self.render("login.html")
    def post(self):
        username = self.get_body_argument("username")
        password = self.get_body_argument("password")
        print(username,password)
        #查询数据
        user=models_manage.UserManager(None,username,password).find_single()
        print("user为：",user,user.name,user.password)
        self.render("index.html")


class RegistHandler(BaseHandler):
    def get(self):
        self.set_cookie("_xsrf","jsdffdssdsdflsdfljjl")
        self.render("regist.html")
    def post(self, *args, **kwargs):
        username=self.get_body_argument("username")
        password=self.get_body_argument("password")
        confirmpsw=self.get_body_argument("confirmpsw")
        print(username,password,confirmpsw)
        #添加数据到数据库
        models_manage.UserManager(None,username,password).create_obj()
        return self.write(json.dumps({
            "status":1,
            "msg":"注册成功",
        }))

