import tornado.web

from . import urls,settings
class Application(tornado.web.Application):
   def __init__(self):
       super(Application,self).__init__(urls.urlpatters,**settings.settings)