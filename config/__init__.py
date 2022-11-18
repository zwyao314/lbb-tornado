from oslo_config import cfg


conf = cfg.CONF

default_opts = [
    cfg.StrOpt(name="name", default="Labuybuy"),
    cfg.StrOpt(name="env", default="PY_APP_ENV"),
    cfg.StrOpt(name="key", default=''),
    cfg.BoolOpt(name="debug", default=True),
    cfg.StrOpt(name="app_url", default="http://localhost"),
    cfg.StrOpt(name="asset_url", default="http://localhost"),
    cfg.StrOpt(name="media_url", default="http://localhost")
]
conf.register_opts(default_opts)

http_server_group = cfg.OptGroup(name="http_server", help="Http server config")
http_server_opts = [
    cfg.StrOpt(name="host", default="127.0.0.1"),
    cfg.IntOpt(name="port", default=8000)
]
conf.register_opts(http_server_opts, group=http_server_group)