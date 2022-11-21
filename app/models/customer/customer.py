from app.models.base_model import BaseModel
from peewee import BigIntegerField, CharField, DateTimeField, IntegerField


class Customer(BaseModel):
    primary_key = "id"

    encid = CharField()
    parent_id = BigIntegerField()
    username = CharField()
    password_hash = CharField()
    cellphone = CharField()
    email = CharField()
    nick_name = CharField()
    full_name = CharField()
    last_name = CharField()
    first_name = CharField()
    state = IntegerField()
    identity = IntegerField()
    avatar = CharField()
    login_count = IntegerField()
    login_at = DateTimeField()
    login_ip = IntegerField()
    login_area_id = BigIntegerField()
    attempts = IntegerField()
    gender = IntegerField()
    date_of_birth = DateTimeField()
    registered_at = DateTimeField()
    registered_ip = IntegerField()
    registered_area_id = BigIntegerField()
    rating_id = BigIntegerField()
    rating_score = IntegerField()
    invite_code = CharField()
    deleted_at = DateTimeField()
    created_at = DateTimeField()
    updated_at = DateTimeField()

    class Meta:
        table_name = BaseModel._meta.table_prefix + "customer"