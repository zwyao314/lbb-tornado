import logging as BaseLogging


class Logging(BaseLogging):

    def to_logger(self, name="logs"):
        logger = self.getLogger(name)
