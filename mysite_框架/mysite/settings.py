from tornado.options import define
import os

Base_dir=os.path.dirname(__file__)
# print("lsdaf",Base_dir)

define("port",default=8011,type=int)

settings={
    "template_path":os.path.join(Base_dir,"templates"),
"static_path": os.path.join( Base_dir,"static"),
    "debug":True,
    #混淆码
    "cookie_secret":"CDRRLwJ5R2Gr5fU16DLwHU8W0lW9kkstjWgJHGJYPbE=",
    #跨域请求伪造攻击
    "xsrf_cookies":True,
    "login_url":"/login"
}