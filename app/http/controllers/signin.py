from config import conf
from tornado.web import RequestHandler
from lib.pymy.hashing.password.scrypt_sha_hasher import ScryptShaHasher
from app.helper.crypt_helper import CryptHelper


class Signin(RequestHandler):
    def get(self):
        # hasher = ScryptShaHasher()
        # hashed_text = hasher.make('123456'.encode())
        # print(hashed_text)

        crypt_helper = CryptHelper(name="DES")
        crypted_text = crypt_helper.encrypt("123456".encode())
        print(crypted_text)
        text = crypt_helper.decrypt(crypted_text)
        print(text)


    def post(self):
        pass