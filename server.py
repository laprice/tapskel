#!/usr/bin/env python

from tornado import web, ioloop, options
import logging
import json
import momoko

class IndexHandler(web.RequestHandler):
    def get(self):
        return self.render('index.html')


def better_logging(handler):
    log_method = logging.info
    request_time = 1000.0 * handler.request.request_time()
    log_method("%s %s %.2fms", handler.get_status(),
               handler._request_summary(), request_time)


if __name__=='__main__':
    import os
    app = web.Application(
        [
            (r'/', IndexHandler),
            (r'/js/(.*)', web.StaticFileHandler, { "path": "./js/" }),
            (r'/css/(.*)', web.StaticFileHandler, { "path": "./css/" }),
            (r'/img/(.*)', web.StaticFileHandler, { "path": "./img/" })
            ],
        debug=True,
        template_path=os.path.join(os.getcwd(),'templates'),
        log_function=better_logging)
    
    options.parse_command_line()
    app.listen(1337)
    ioloop.IOLoop.instance().start()
