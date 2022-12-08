from abc import ABCMeta, abstractmethod


class AbstractCaptcha(metaclass=ABCMeta):

    # Generates a captcha, and return captcha URL
    @abstractmethod
    def generate(self) -> str:
        pass

    @abstractmethod
    def validate_phrase(self, user_phrase: str) -> bool:
        pass

    # Finds captcha code from this ID.
    @abstractmethod
    def get_id(self) -> str:
        pass