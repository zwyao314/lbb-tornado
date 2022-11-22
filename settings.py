from app.http.middleware import (
    locale
)


middlewares = [
    locale.Locale()
]