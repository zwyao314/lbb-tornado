import base64
from config import conf
from Crypto.Cipher import AES, DES, DES3
from lib.pymy.hashing.block_cipher import BlockCipher
from random import randbytes


class CryptHelper(object):
    def __init__(self, name: str, mode: str = "cbc"):
        self.__name = name.lower()
        self.__cipher = None
        self.__mode = mode
        self.__key = CryptHelper.parse_key(conf)

    @staticmethod
    def generate_key() -> bytes:
        b_key = randbytes(48)
        b_key = base64.b64encode(b_key)
        b_key = "base64:".encode() + b_key

        return b_key

    @staticmethod
    def parse_key(config: conf) -> bytes:
        key = conf.app_key
        b_key = key.encode()
        prefix = "base64:"
        if key.startswith(prefix):
            key = key.replace(prefix, '')
            b_key = base64.b64decode(key)

        return b_key

    def __new_cipher(self):
        cipher = BlockCipher(self.__name)
        cipher.set_key(self.__key)\
            .set_mode(self.__mode)

        return cipher

    def __get_cipher(self):
        cipher = self.__cipher
        if cipher is None:
            cipher = self.__new_cipher()
            self.__cipher = cipher

        return cipher

    def encrypt(self, text: bytes) -> bytes:
        cipher = self.__get_cipher()
        crypted_text = cipher.encrypt(text)

        return crypted_text

    def decrypt(self, crypted_text: bytes) -> bytes:
        cipher = self.__get_cipher()
        text = cipher.decrypt(crypted_text)

        return text
