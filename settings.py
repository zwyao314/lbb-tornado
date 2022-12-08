from lib.pymy.i18n import locale_middleware
from lib.pymy.session import session_middleware


middlewares = [
    locale_middleware.LocaleMiddleware(),
    session_middleware.SessionMiddleware(),
]