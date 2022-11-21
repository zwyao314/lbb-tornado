from app.models.base_model import BaseModel


class Customer(BaseModel):
    primary_key = "id"

    class Meta:
        table_name = BaseModel._meta.table_prefix + "customer"