from tornado.web import RequestHandler


class NotFound(RequestHandler):
    def get(self):
        self.set_status(404)
        self.write(self.locale.translate("404 Not found page"))