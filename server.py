# -*- coding: utf-8 -*- 

from tornado.ioloop import IOLoop
from tornado.options import parse_command_line
from tornado.web import Application

from settings import SETTINGS, PORT
from apps.main.handlers import IndexHandler

class ViberApplication(Application):
    def __init__(self):

        handlers = (
            (r"/", IndexHandler),    
        )

        # application set 
        Application.__init__(self, handlers, **SETTINGS)

parse_command_line()
ViberApplication().listen(PORT)
IOLoop.instance().start()
