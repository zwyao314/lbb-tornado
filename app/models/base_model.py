from config import conf
from peewee import Model, MySQLDatabase

db_params = {
    "host": conf.mysql.host,
    "port": conf.mysql.port,
    "user": conf.mysql.username,
    "password": conf.mysql.password,
    "unix_socket": conf.mysql.unix_socket
}
db = MySQLDatabase(
    database=conf.mysql.database,
    **db_params
)


# Base model
class BaseModel(Model):
    class Meta:
        database = db
        table_prefix = conf.mysql.prefix