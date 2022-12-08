from constant import ROOT_PATH
from lib.pymy.http.middleware.base_middleware import BaseMiddleware
from os.path import dirname, join as path_join, realpath
from tornado import locale
from tornado.web import RequestHandler


# Locale middleware
class LocaleMiddleware(BaseMiddleware):
    def process_request(self, handler: RequestHandler):
        request = handler.request
        language = request.headers.get("Accept-Language")
        langPart = language.split(',')
        lang = langPart[0][:2]
        locale.set_default_locale(lang)
        locale.load_translations(path_join(ROOT_PATH, "resources", "lang", lang))

    def process_response(self, handler: RequestHandler):
        pass
