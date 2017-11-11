'''
路由配置
'''

from . import views
urlpatters=[
    (r"/",views.IndexHandler),

    (r"/login",views.LoginHandler),

    (r"/regist",views.RegistHandler) ,
]