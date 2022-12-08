import logging
from constant import ROOT_PATH
from os.path import join as path_join


class Log(object):
    loggers = {}

    @classmethod
    def to_logger(cls, name="logs"):
        logger = cls.loggers[name] if name in cls.loggers else None
        if logger is None:
            logger = logging.getLogger(name)
            handler = logging.FileHandler(
                filename=path_join(ROOT_PATH, "runtime", "logs", name+".log")
            )
            handler.setFormatter(
                logging.Formatter(
                    fmt='''
Thread ID: %(thread)d
Created at: %(created)f
%(levelname)s: %(message)s in %(pathname)s, line %(lineno)d
Function: %(funcName)s
                    '''
                )
            )
            logger.addHandler(handler)
            cls.loggers[name] = logger

        return logger

    @classmethod
    def to_error_logger(cls):
        return cls.to_logger("logs_error")
