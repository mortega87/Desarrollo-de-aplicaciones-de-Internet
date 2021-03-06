# encoding: utf-8

import web
from web.contrib.template import render_mako

urls = ( '/(.*)', 'hello' )

app = web.application(urls, globals(), autoreload=True)

plantillas = render_mako(
        directories=['templates'],
        input_encoding='utf-8',
        output_encoding='utf-8'
        )

class hello:
    def GET(self, name):
        return plantillas.hello(nombre=name)

if __name__ == "__main__":
    app.run()
