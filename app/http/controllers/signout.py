import tornado.routing
from app.helper.crypt_helper import CryptHelper
from app.http.controllers.base_handler import BaseHandler


class Signout(BaseHandler):
    def get(self):
        crypt_helper = CryptHelper(name="DES")
        crypted_text = b'y\x19\x00\xf8\xf8+%\x8e'
        text = crypt_helper.decrypt(crypted_text)
        print(text)
