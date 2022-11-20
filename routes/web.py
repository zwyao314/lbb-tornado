from app.http.controllers import (
    signin,
    signout
)
from tornado.web import url

routes = []
routes.extend([
    url(r"/sign/in", signin.Signin, name="signin"),
    url(r"/sign/in-post", signin.Signin, name="signin.post"),
    url(r"/sign/out", signout.Signout, name="signout")
])