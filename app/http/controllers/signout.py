from tornado.web import RequestHandler
from app.helper.crypt_helper import CryptHelper

class Signout(RequestHandler):
    def get(self):
        crypt_helper = CryptHelper(name="DES")
        crypted_text = b'y\x19\x00\xf8\xf8+%\x8e'
        text = crypt_helper.decrypt(crypted_text)
        print(text)
