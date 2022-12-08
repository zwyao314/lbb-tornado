import json
import settings
from helpers import asset_url, media_url, skin_path
from typing import Any, Awaitable, Dict, List, Optional, Union
from tornado.web import RequestHandler
from torndsession.sessionhandler import SessionBaseHandler


class BaseHandler(SessionBaseHandler):
    def initialize(self, **kwargs: Any) -> None:
        middlewares = kwargs["middlewares"] if "middlewares" in kwargs else []
        default_middlewares = self.__get_default_middlewares()
        self.middlewares = default_middlewares + middlewares
        super(BaseHandler, self).initialize(**kwargs)

    def prepare(self) -> Optional[Awaitable[None]]:
        for middleware in self.middlewares:
            middleware.process_request(self)

        return super(BaseHandler, self).prepare()

    def on_finish(self) -> None:
        super(BaseHandler, self).on_finish()

        for middleware in self.middlewares:
            middleware.process_response(self)

    def get_template_namespace(self) -> Dict[str, Any]:
        namespace = super(BaseHandler, self).get_template_namespace()
        namespace.update({
            "asset_url": asset_url,
            "media_url": media_url,
            "skin_path": skin_path
        })

        return namespace

    def __get_default_middlewares(self):
        default_middlewares = settings.middlewares

        return default_middlewares

    # self.locale.translate alias
    def _(
            self,
            message: str,
            plural_message: str = None,
            count: int = None
    ):
        return self.locale.translate(message, plural_message, count)

    def json_response(
            self,
            status: int,
            message: str,
            data: Optional[Union[Dict, List, Any]] = None
    ):
        if not len(data):
            data = None
        result = {
            "code": status,
            "msg": message,
            "data": data
        }
        result = json.dumps(result)

        self.set_header("Content-Type", "application/json")
        self.write(result)

