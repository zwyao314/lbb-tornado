import base64


class UrlHelper(object):
    @staticmethod
    def url_encode(url: bytes) -> bytes:
        encoded_url = base64.b64encode(url)
        trans_table = str.maketrans('+/=', '-_,')
        encoded_url = encoded_url.translate(trans_table)

        return encoded_url

    @staticmethod
    def url_decode(encoded_url: bytes) -> bytes:
        trans_table = str.maketrans('-_,', '+/=')
        encoded_url = encoded_url.translate(trans_table)
        url = base64.b64decode(encoded_url)

        return url
