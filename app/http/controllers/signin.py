from app.http.controllers.base_handler import BaseHandler
from app.models.customer.customer import Customer


class Signin(BaseHandler):
    def get(self):
        # fields = [
        #     "id",
        #     "username",
        #     "password_hash"
        # ]
        # ones = Customer.select(*fields).where(Customer._meta.primary_key == 10000)
        one = Customer.get_by_id(10000)
        print(one.created_at)
        print(one.updated_at)
        data = {
            "title": "Sign in",
            "page_title": "Sign in"
        }
        return self.render("default/default/customer/signin.html", **data)

    def post(self):
        print("Signin Post")