import asyncio
from asyncio.exceptions import CancelledError
from app.helper.crypt_helper import CryptHelper
from app.http.controllers.not_found import NotFound as NotFoundHandler
from config import conf
from constant import ROOT_PATH
from lib.pymy.logging.log import Log
from os import mkdir
from os.path import isdir, join as path_join
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
            "static_path": path_join(ROOT_PATH, "resources", "static"),
            "cookie_secret": CryptHelper.parse_key(conf),
            "xsrf_cookies": True
        }
        session_settings = {
            "driver": conf.session.driver,
            "driver_settings": {
                "host": conf.session.host,
                "prefix": conf.session.prefix
            },
            "force_persistence": True,
            "sid_name": conf.session.sid_name,
            "session_lifetime": conf.session.lifetime
        }
        settings.update(session=session_settings)
        super(WebApplication, self).__init__(handlers=handlers, **settings)


def make_app() -> WebApplication:
    app = WebApplication(handlers=web_routes)
    # Init dirs
    resources_path = path_join(ROOT_PATH, "resources")
    runtime_path = path_join(ROOT_PATH, "runtime")
    if not isdir(resources_path):
        mkdir(resources_path, mode=0o777)
    if not isdir(runtime_path):
        mkdir(runtime_path, mode=0o777)

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


# def fork_main():
#     pass


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        pass
    # except CancelledError as e:
    #     pass
    except BaseException as e:
        print(f"Exception: {e}")
        Log.to_error_logger().exception(e)
