from config import conf
from peewee import Model
from playhouse.pool import PooledMySQLDatabase
db_params = {
    "host": conf.mysql.host,
    "port": conf.mysql.port,
    "user": conf.mysql.username,
    "password": conf.mysql.password,
    "unix_socket": conf.mysql.unix_socket,
    "charset": conf.mysql.charset,
    "max_connections": conf.mysql.max_connections,
    "stale_timeout": 300
}
db = PooledMySQLDatabase(
    database=conf.mysql.database,
    **db_params
)
PooledMySQLDatabase.field_types["JSON"] = "JSON"


# Base model
class BaseModel(Model):
    class Meta:
        database = db
        legacy_table_names = False
        table_prefix = conf.mysql.prefix