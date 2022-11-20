from app.http.controllers.base_handler import BaseHandler


class Signin(BaseHandler):
    def get(self):
        data = {
            "title": "Sign in",
            "page_title": "Sign in"
        }
        return self.render("default/default/user/signin.html", **data)

    def post(self):
        print("Signin Post")