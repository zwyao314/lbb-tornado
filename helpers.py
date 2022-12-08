import hashlib
import random
from config import conf
from lib.pymy.session.session import Session
from lib.pymy.stdlib.date_time import DateTime


def session(key=None, value=None):
    session = Session.session()
    if key is None:
        return session
    elif value is None:
        return session.get(key)
    elif value is not None:
        session.set(key, value)


def session_delete(key):
    session = Session.session()
    value = session.get(key, default=None)
    session.delete(key)

    return value


def unique_hash_id() -> str:
    b_hash_text = str(DateTime.now()).encode() + '|'.encode() + random.randbytes(40)
    id = hashlib.md5(b_hash_text).hexdigest()

    return id


def asset_url(path: str = None) -> str:
    assetUrl = conf.asset_url
    assetUrl += '/static'
    if path is not None:
        path = '/' + path.lstrip('/')
        assetUrl += path

    return assetUrl


def media_url(path: str = None) -> str:
    mediaUrl = conf.media_url
    mediaUrl += '/static/media'
    if path is not None:
        path = '/' + path.lstrip('/')
        mediaUrl += path

    return mediaUrl


def skin_path(path: str = None) -> str:
    skinPath = "skin/"
    skinPath += "default/default"
    if path is not None:
        path = '/' + path.lstrip('/')
        skinPath += path

    return skinPath
