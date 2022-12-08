from lib.pymy.captcha.concern.abstract_captcha import AbstractCaptcha
from abc import abstractmethod


class AbstractImageCaptcha(AbstractCaptcha):

    @abstractmethod
    def get_width(self) -> int:
        pass

    @abstractmethod
    def get_height(self) -> int:
        pass