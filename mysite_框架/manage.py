"""
项目启动：
    使用命令python manage.py 启动我们的tornado
"""
from mysite import base
from tornado.options import options
from tornado.ioloop import IOLoop

if __name__ =="__main__":
    #创建一个项目应用
    app = base.Application()
    #监听
    app.listen(options.port)
    #启动
    IOLoop.current().start()