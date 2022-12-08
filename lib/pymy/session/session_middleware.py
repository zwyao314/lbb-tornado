from lib.pymy.http.middleware.base_middleware import BaseMiddleware
from lib.pymy.session.session import Session
from tornado.web import RequestHandler


class SessionMiddleware(BaseMiddleware):

    def process_request(self, handler: RequestHandler):
        Session.bind(handler.session)

    def process_response(self, handler: RequestHandler):
        pass