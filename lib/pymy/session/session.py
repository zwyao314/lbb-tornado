from typing import Optional, Union
from torndsession.session import SessionManager


class Session(object):
    sess = None

    @classmethod
    def bind(cls, session: SessionManager):
        cls.sess = session

        return cls

    @classmethod
    def session(cls) -> Optional[Union[SessionManager, None]]:
        return cls.sess