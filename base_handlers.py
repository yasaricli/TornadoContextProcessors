# -*- coding: utf-8 -*- 

from tornado.web import RequestHandler
from processors import request_context

class BaseHandler(RequestHandler):
    """
        class Handler(BaseHandler):
            def get(self):
                ctc = {
                    "a": "b" ,
                    "c": "d"   
                }
                self.rebder_to_response("handler.html", ctx)
    """
    def render_to_response(self, template, context):
        ctx = request_context(self)
        context.update(ctx)
        self.render(template, **context)
