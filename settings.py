# -*- coding: utf-8 -*- 

import os

PORT = 8989

CONTEXT_PROCESSORS = (
    "apps.main.context_processors.main",
)

SETTINGS = dict(
    debug=True,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static")    
)
