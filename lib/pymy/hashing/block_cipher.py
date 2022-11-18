from Crypto.Cipher import AES, DES, DES3
from Crypto.Util.Padding import pad, unpad


class BlockCipher(object):
    def __init__(self, name: str):
        self.__name = name.lower()
        self.__cipher = None
        self.__decipher = None
        self.__key = None
        self.__mode = "cbc"

    def get_name(self):
        return self.__name

    def set_key(self, key: bytes):
        self.__key = key

        return self

    def get_key(self) -> bytes:
        return self.__key

    def set_mode(self, mode: str):
        self.__mode = mode.lower()

        return self

    def get_mode(self) -> str:
        return self.__mode

    def __new_cipher(self):
        match self.__name:
            case "aes":
                key = self.__key[:AES.key_size[-1]]
                match self.__mode:
                    case "ecb":
                        mode = AES.MODE_ECB
                    case "cbc":
                        mode = AES.MODE_CBC
                    case "cfb":
                        mode = AES.MODE_CFB
                    case "ofb":
                        mode = AES.MODE_OFB
                    case "ctr":
                        mode = AES.MODE_CTR
                    case "openpgp":
                        mode = AES.MODE_OPENPGP
                    case "ccm":
                        mode = AES.MODE_CCM
                    case "eax":
                        mode = AES.MODE_EAX
                    case "gcm":
                        mode = AES.MODE_GCM
                    case "siv":
                        mode = AES.MODE_SIV
                    case "ocb":
                        mode = AES.MODE_OCB
                    case _:
                        mode = AES.MODE_CBC

                cipher = AES.new(key, mode)
            case "des":
                key = self.__key[:DES.key_size]
                match self.__mode:
                    case "ecb":
                        mode = AES.MODE_ECB
                    case "cbc":
                        mode = AES.MODE_CBC
                    case "cfb":
                        mode = AES.MODE_CFB
                    case "ofb":
                        mode = AES.MODE_OFB
                    case "ctr":
                        mode = AES.MODE_CTR
                    case "openpgp":
                        mode = AES.MODE_OPENPGP
                    case "eax":
                        mode = AES.MODE_EAX
                    case _:
                        mode = AES.MODE_CBC

                cipher = DES.new(key, mode)
            case "des3":
                key = self.__key[:DES3.key_size[-1]]
                match self.__mode:
                    case "ecb":
                        mode = AES.MODE_ECB
                    case "cbc":
                        mode = AES.MODE_CBC
                    case "cfb":
                        mode = AES.MODE_CFB
                    case "ofb":
                        mode = AES.MODE_OFB
                    case "ctr":
                        mode = AES.MODE_CTR
                    case "openpgp":
                        mode = AES.MODE_OPENPGP
                    case "eax":
                        mode = AES.MODE_EAX
                    case _:
                        mode = AES.MODE_CBC

                cipher = DES3.new(key, mode)

        return cipher

    def __get_cipher(self):
        cipher = self.__cipher
        if cipher is None:
            cipher = self.__new_cipher()
            self.__cipher = cipher

        return cipher

    def encrypt(self, text: bytes) -> bytes:
        cipher = self.__get_cipher()
        text = pad(text, cipher.block_size)
        crypted_text = cipher.encrypt(text)

        return crypted_text

    def __get_decipher(self):
        decipher = self.__decipher
        if decipher is None:
            decipher = self.__new_cipher()
            self.__decipher = decipher

        return decipher

    def decrypt(self, crypted_text: bytes) -> bytes:
        decipher = self.__get_decipher()
        text = decipher.decrypt(crypted_text)
        print(text)
        text = unpad(text, decipher.block_size)

        return text
