Tornado context processors 
===========================
___________________________

### ` CONTEXT_PROCESSORS `

#### app/main/context_processors.py
```python
def main(handler):
    return {
        'say_hello':"Hello I main application context",
        # context
    }
```

#### settings.py
```python
CONTEXT_PROCESSORS = (
    "apps.main.context_processors.main",
)
```

### ` CONTEXT_PROCESSORS Handler`

#### render_to_response method BaseHandler 
```python
from base_handlers import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        ctx = {
            "handler_name": "IndexHandler",
        }
        self.render_to_response("index.html", ctx)
```
