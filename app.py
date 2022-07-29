# -*- coding = UTF-8 -*-

from tornado import web, ioloop, httpserver


class MainPageHandler(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render('./static/index.html')


application = web.Application([(r"/", MainPageHandler), ])

if __name__ == '__main__':
    httpserver = httpserver.HTTPServer(application)
    httpserver.listen(8080)
    ioloop.IOLoop.current().start()
