from app.http.controllers.base_handler import BaseHandler
from app.models.customer.customer import Customer


class Signin(BaseHandler):
    def get(self):
        fields = [
            Customer.id,
            Customer.username,
            Customer.password_hash
        ]
        query = Customer.select(*fields).where(Customer._meta.primary_key == 10000)
        one = query.get()
        print(query.sql())
        print(one.username)
        print(one.id)

        data = {
            "title": "Sign in",
            "page_title": "Sign in"
        }

        return self.render("customer/signin.html", **data)

    def post(self):
        print("Signin Post")