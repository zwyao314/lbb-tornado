import asyncio
import logging
from app.http.controllers.signin import Signin as SigninHandler
from app.http.controllers.signout import Signout as SignoutHandler
from config import cfg
from tornado.options import define, options
from tornado.web import Application, HTTPServer

conf = cfg.CONF

define("port", default=conf.http_server.port, type=int, help="Running the http server on the port")


class WebApplication(Application):
    def __init__(self, handlers: list = None):
        super(WebApplication, self).__init__(handlers=handlers)


def make_app() -> WebApplication:
    app = WebApplication([
        (r"/sign/in", SigninHandler),
        (r"/sign/out", SignoutHandler)
    ])

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