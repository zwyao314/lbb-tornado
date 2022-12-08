import base64
import hashlib


class ScryptShaHasher(object):
    # Crypt password
    def make(self, text: bytes, salt: bytes) -> bytes:
        b_hashed_text = self.__crypt_text(text)
        salt = salt[:32]
        b_hashed_text = hashlib.scrypt(
            password=b_hashed_text,
            salt=salt,
            n=len(salt),
            r=2,
            p=3
        )
        b_hashed_text = base64.b64encode(b_hashed_text)

        return b_hashed_text

    # verify password
    def check(self, text: bytes, hashed_text: bytes, salt: bytes) -> bool:
        return hashed_text == self.make(text, salt=salt)

    # Sha3_256 crypt text
    def __crypt_text(self, text: bytes) -> bytes:
        sha256 = hashlib.sha3_256(text)

        return sha256.hexdigest().encode()