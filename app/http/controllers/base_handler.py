from app.http.middleware.locale import Locale as LocaleMiddleware
from asyncio.futures import Future
from os.path import join as path_join
from typing import Any, Awaitable, Optional, Union
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def initialize(self, **kwargs: Any) -> None:
        middlewares = kwargs["middlewares"] if "middlewares" in kwargs else []
        default_middlewares = self._get_default_middlewares()
        self.middlewares = default_middlewares + middlewares
        super(BaseHandler, self).initialize(**kwargs)

    def _get_default_middlewares(self):
        default_middlewares = [
            LocaleMiddleware()
        ]

        return default_middlewares

    def prepare(self) -> Optional[Awaitable[None]]:
        for middleware in self.middlewares:
            middleware.process_request(self)

        return super(BaseHandler, self).prepare()

    def finish(self, chunk: Optional[Union[str, bytes, dict]] = None) -> "Future[None]":
        result = super(BaseHandler, self).finish(chunk)

        for middleware in self.middlewares:
            middleware.process_response(self)

        return result