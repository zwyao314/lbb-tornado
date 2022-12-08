from app.helper.crypt_helper import CryptHelper
from config import conf
from lib.pymy.hashing.password.scrypt_sha_hasher import ScryptShaHasher


class UserService(object):
    hasher = ScryptShaHasher()

    @classmethod
    def password_hash(cls, password: str) -> str:
        hasher = cls.hasher
        key = CryptHelper.parse_key(conf)
        b_hash = hasher.make(password.encode(), salt=key.encode())

        return b_hash.decode(encoding=conf.byte_encoding)

    '''
        :param: password, str
        :param: password_hash, str
        :return: bool
    '''
    @classmethod
    def verify_password(cls, password: str, password_hash: str) -> bool:
        hasher = cls.hasher
        key = CryptHelper.parse_key(conf)

        return hasher.check(password.encode(), hashed_text=password_hash.encode(), salt=key.encode())