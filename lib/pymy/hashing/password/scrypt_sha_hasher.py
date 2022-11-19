import base64
from hashlib import scrypt, sha3_256
from random import randbytes


class ScryptShaHasher(object):
    # Crypt password
    def make(self, text: bytes, key: bytes) -> bytes:
        hashed_text = self.__crypt_text(text)
        key = key[:32]
        b_hashed_text = scrypt(
            password=hashed_text,
            salt=key,
            n=len(key),
            r=2,
            p=3
        )
        b_hashed_text = base64.b64encode(b_hashed_text)

        return b_hashed_text

    # verify password
    def check(self, text: bytes, hashed_text: bytes, key: bytes) -> bool:
        return hashed_text == self.make(text, key)

    # Sha3_256 crypt text
    def __crypt_text(self, text: bytes) -> bytes:
        sha256 = sha3_256()
        sha256.update(text)

        return sha256.hexdigest().encode()