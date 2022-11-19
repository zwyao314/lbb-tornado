from config import conf
from tornado.web import RequestHandler
from lib.pymy.hashing.password.scrypt_sha_hasher import ScryptShaHasher
from app.helper.crypt_helper import CryptHelper


# test code
class Crypt(RequestHandler):
    def get(self):
        hasher = ScryptShaHasher()
        b_hashed_text = hasher.make(
            "123456".encode(),
            key=CryptHelper.parse_key(conf).encode()
        )
        b_hashed_text2 = hasher.make(
            "123456".encode(),
            key=CryptHelper.parse_key(conf).encode()
        )
        print(b_hashed_text)
        print(b_hashed_text2)

        # crypt_helper = CryptHelper(name="DES", mode="cbc")
        # crypted_text = crypt_helper.encrypt("123456")
        # print(crypted_text)
        # text = crypt_helper.decrypt(crypted_text)
        # print(text)
