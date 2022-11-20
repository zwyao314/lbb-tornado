from app.http.middleware.base_middleware import BaseMiddleware
from constant import ROOT_PATH
from os.path import dirname, join as path_join, realpath
from tornado import locale
from tornado.web import RequestHandler


# Locale middleware
class Locale(BaseMiddleware):
    def process_request(self, handler: RequestHandler):
        request = handler.request
        language = request.headers.get("Accept-Language")
        langPart = language.split(',')
        lang = langPart[0][:2]
        locale.set_default_locale(lang)
        locale.load_translations(path_join(ROOT_PATH, "resources", "lang", lang))
