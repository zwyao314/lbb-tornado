from oslo_config import cfg
from os import environ
from os.path import dirname, join as path_join, realpath

conf = cfg.CONF

default_opts = [
    cfg.StrOpt(name="app_name", default="Labuybuy"),
    cfg.StrOpt(name="app_env", default="PY_APP_ENV"),
    cfg.StrOpt(name="app_key", default=''),
    cfg.BoolOpt(name="app_debug", default=True),
    cfg.StrOpt(name="app_url", default="http://localhost"),
    cfg.StrOpt(name="asset_url", default="http://localhost"),
    cfg.StrOpt(name="media_url", default="http://localhost"),
    cfg.StrOpt(name="byte_encoding", default="UTF-8")
]
conf.register_opts(default_opts)

http_server_group = cfg.OptGroup(name="http_server", help="Http server config")
http_server_opts = [
    cfg.StrOpt(name="host", default="127.0.0.1"),
    cfg.IntOpt(name="port", default=8000)
]
conf.register_group(http_server_group)
conf.register_opts(http_server_opts, group=http_server_group)

mysql_group = cfg.OptGroup(name="mysql", help="MySQL config")
mysql_opts = [
    cfg.StrOpt(name="url", default="mysql://root:password@host:port/database?charset=utf8")
]
conf.register_group(mysql_group)
conf.register_opts(mysql_opts, mysql_group)

redis_group = cfg.OptGroup(name="redis", help="Redis config")
redis_opts = [
    cfg.StrOpt(name="host", default="127.0.0.1"),
    cfg.StrOpt(name="password", default=''),
    cfg.IntOpt(name="port", default=6379)
]
conf.register_group(redis_group)
conf.register_opts(redis_opts, redis_group)

rabbitmq_group = cfg.OptGroup(name="rabbitmq", help="Rabbitmq config")
rabbitmq_opts = [
    cfg.StrOpt(name="url", default="amqp://user:password@host:port//vhost")
]

env = environ.get(conf.app_env, default="development")
config_file = path_join(dirname(realpath(__file__)), env+".conf")
conf(default_config_files=[config_file])
