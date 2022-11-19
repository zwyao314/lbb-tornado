import asyncio
import logging
from app.http.controllers.crypt import Crypt as CryptHandler
from app.http.controllers.not_found import NotFound as NotFoundHandler
from app.http.controllers.signin import Signin as SigninHandler
from config import conf
from app.helper.crypt_helper import CryptHelper
from os.path import dirname, join as path_join, realpath
from tornado import locale
from tornado.options import define, options
from tornado.web import Application, HTTPServer

define("port", default=conf.http_server.port, type=int, help="Running the http server on the port")


class WebApplication(Application):
    def __init__(self, handlers: list = None):
        root_path = dirname(realpath(__file__))
        settings = {
            "debug": conf.app_debug,
            "default_handler_class": NotFoundHandler,
            "template_path": path_join(root_path, "resources/views"),
            "static_path": path_join(root_path, "resources/static"),
            "cookie_secret": CryptHelper.parse_key(conf)
        }
        super(WebApplication, self).__init__(handlers=handlers, **settings)


def make_app() -> WebApplication:
    root_path = dirname(realpath(__file__))
    app = WebApplication(
        [
            (r"/sign/in", SigninHandler),
            (r"/crypt", CryptHandler)
        ]
    )
    locale.set_default_locale("zh")
    locale.load_translations(path_join(root_path, "resources/lang"))

    return app


async def main():
    app = make_app()
    http_server = HTTPServer(app, xheaders=True)
    http_server.listen(port=options.port, address=conf.http_server.host)
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