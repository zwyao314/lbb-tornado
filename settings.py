from app.http.middleware import (
    locale_middleware
)


middlewares = [
    locale_middleware.LocaleMiddleware()
]