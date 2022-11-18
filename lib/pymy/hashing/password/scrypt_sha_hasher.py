from hashlib import scrypt, sha3_256


class ScryptShaHasher(object):
    # Crypt password
    def make(self, text: bytes, key: bytes = b'') -> bytes:
        hashed_text = self.__crypt_text(text)
        print(hashed_text)
        hashed_text = scrypt(hashed_text, salt=key)

        return hashed_text

    # verify password
    def check(self, text: bytes, hashed_text: bytes, key: bytes = b'') -> bool:
        return hashed_text == self.make(text, key)

    # Sha3_256 crypt text
    def __crypt_text(self, text: bytes) -> bytes:
        sha256 = sha3_256()
        sha256.update(text)

        return sha256.hexdigest().encode()