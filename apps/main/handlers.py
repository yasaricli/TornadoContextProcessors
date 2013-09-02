# -*- coding: utf-8 -*- 

from base_handlers import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        ctx = {
            "handler_name": "IndexHandler",
        }
        self.render_to_response("index.html", ctx)
