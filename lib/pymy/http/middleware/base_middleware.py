from abc import ABCMeta, abstractmethod
from tornado.web import RequestHandler


class BaseMiddleware(metaclass=ABCMeta):

    @abstractmethod
    def process_request(self, handler: RequestHandler):
        pass

    @abstractmethod
    def process_response(self, handler: RequestHandler):
        pass