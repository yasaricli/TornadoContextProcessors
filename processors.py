# -*- coding: utf-8 -*- 

import sys
from settings import CONTEXT_PROCESSORS

def request_context(handler_self):
    """
        CONTEXT_PROCESSORS REQUEST
    """
    context = {}
    for ctx_path in CONTEXT_PROCESSORS:
        fnc = import_by_path(ctx_path)(handler_self)
        context.update(fnc)
    return context

def import_by_path(dotted_path):
    """
        module path function import 
    """
    module_path, class_name = dotted_path.rsplit('.', 1)
    module = import_module(module_path)
    attr = getattr(module, class_name)
    return attr

def import_module(name, package=None):
    """
        Import a module.
    """
    if name.startswith('.'):
        if not package:
            raise TypeError("relative imports require the 'package' argument")
        level = 0
        for character in name:
            if character != '.':
                break
            level += 1
        name = _resolve_name(name[level:], package, level)
    __import__(name)
    return sys.modules[name]
