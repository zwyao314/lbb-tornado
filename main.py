import asyncio
import logging
from app.helper.crypt_helper import CryptHelper
from app.http.controllers.not_found import NotFound as NotFoundHandler
from config import conf
from constant import ROOT_PATH
from os.path import join as path_join
from routes.web import routes as web_routes
from tornado.options import define, options
from tornado.web import Application

define("port", default=conf.http_server.port, type=int, help="Running the http server on the port")


class WebApplication(Application):
    def __init__(self, handlers: list = None):
        skin_path = "default/default"
        settings = {
            "debug": conf.app_debug,
            "default_handler_class": NotFoundHandler,
            "template_path": path_join(ROOT_PATH, "resources", "views", "skin", skin_path),
            "static_path": path_join(ROOT_PATH, "resources", "static", "skin", skin_path),
            "cookie_secret": CryptHelper.parse_key(conf),
            "xsrf_cookies": True
        }
        super(WebApplication, self).__init__(handlers=handlers, **settings)


def make_app() -> WebApplication:
    app = WebApplication(handlers=web_routes)

    return app


async def main():
    app = make_app()
    http_server = app.listen(
        port=options.port,
        address=conf.http_server.host,
        xheaders=True
    )
    shutdown_event = asyncio.Event()
    print(f"Running http server on the host: {conf.http_server.host}:{conf.http_server.port}")

    await shutdown_event.wait()


def fork_main():
    pass


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except BaseException as e:
        logging.exception(e)
        print(f"Exception: {e}")