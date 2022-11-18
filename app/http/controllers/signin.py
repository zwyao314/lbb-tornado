from tornado.web import RequestHandler
from lib.pymy.hashing.password.scrypt_sha_hasher import ScryptShaHasher


class Signin(RequestHandler):
    def get(self):
        hasher = ScryptShaHasher()
        hashed_text = hasher.make('123456'.encode())
        print(hashed_text)

    def post(self):
        pass