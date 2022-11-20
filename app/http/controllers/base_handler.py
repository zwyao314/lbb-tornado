from app.http.middleware.locale import Locale as LocaleMiddleware
from typing import Any
from tornado.httputil import HTTPServerRequest
from tornado.web import Application, RequestHandler


class BaseHandler(RequestHandler):
    def initialize(
            self,
            middlewares: list = [],
            **kwargs: Any
    ) -> None:
        default_middlewares = [
            LocaleMiddleware()
        ]
        self.middlewares = default_middlewares + middlewares
        super(BaseHandler, self).initialize(**kwargs)

    def prepare(self) -> None:
        for middleware in self.middlewares:
            middleware.process_request(self)
