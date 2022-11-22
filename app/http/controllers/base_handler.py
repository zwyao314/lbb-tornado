import settings
from asyncio.futures import Future
from typing import Any, Awaitable, Optional, Union
from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    def initialize(self, **kwargs: Any) -> None:
        middlewares = kwargs["middlewares"] if "middlewares" in kwargs else []
        default_middlewares = self._get_default_middlewares()
        self.middlewares = default_middlewares + middlewares
        super(BaseHandler, self).initialize(**kwargs)

    def _get_default_middlewares(self):
        default_middlewares = settings.middlewares

        return default_middlewares

    def prepare(self) -> Optional[Awaitable[None]]:
        for middleware in self.middlewares:
            middleware.process_request(self)

        return super(BaseHandler, self).prepare()

    def on_finish(self) -> None:
        super(BaseHandler, self).on_finish()

        for middleware in self.middlewares:
            middleware.process_response(self)