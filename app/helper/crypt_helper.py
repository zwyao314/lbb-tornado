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
    def generate_key() -> str:
        b_key = randbytes(48)
        b_key = base64.b64encode(b_key)
        key = b_key.decode()
        key = "base64:" + key

        return key

    @staticmethod
    def parse_key(config: conf) -> str:
        key = conf.app_key
        prefix = "base64:"
        if key.startswith(prefix):
            key = key.replace(prefix, '')
            b_key = base64.b64decode(key)
            key = b_key.decode(encoding=conf.byte_encoding)

        return key

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

    def encrypt(self, text: str) -> str:
        cipher = self.__get_cipher()
        text = text.encode()
        b_crypted_text = cipher.encrypt(text)
        b_crypted_text = base64.b64encode(b_crypted_text)
        crypted_text = b_crypted_text.decode()

        return crypted_text

    def decrypt(self, crypted_text: str) -> str:
        cipher = self.__get_cipher()
        b_crypted_text = base64.b64decode(crypted_text)
        b_text = cipher.decrypt(b_crypted_text)
        text = b_text.decode(encoding=conf.byte_encoding)

        return text
