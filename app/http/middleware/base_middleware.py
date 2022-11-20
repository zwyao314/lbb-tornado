from tornado.web import RequestHandler


class BaseMiddleware(object):
    def process_request(self, handler: RequestHandler):
        pass

    def process_response(self, handler: RequestHandler):
        pass