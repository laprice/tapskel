#!/usr/bin/env python

from tornado import web, ioloop
import json
import momoko

class IndexHandler(web.RequestHandler):
    def get(self):
        return self.render('templates/index.html')


if __name__=='__main__':
    app = web.Application(
        [
            (r'/', IndexHandler),
            (r'/js/(.*)', web.StaticFileHandler, { "path": "./js/" }),
            (r'/css/(.*)', web.StaticFileHandler, { "path": "./css/" }),
            (r'/img/(.*)', web.StaticFileHandler, { "path": "./img/" })
            ],
        debug=True)
    app.listen(1337)
    ioloop.IOLoop.instance().start()
