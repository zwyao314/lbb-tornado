from app.http.controllers.base_handler import BaseHandler
from app.models.customer.customer import Customer


class Signin(BaseHandler):
    def get(self):
        # one = Customer.select(*[
        #     "id",
        #     "username",
        #     "password"
        # ]).where("id" == 1).get()
        one = Customer.get_by_id(*[1])
        print(one)
        data = {
            "title": "Sign in",
            "page_title": "Sign in"
        }
        return self.render("default/default/customer/signin.html", **data)

    def post(self):
        print("Signin Post")