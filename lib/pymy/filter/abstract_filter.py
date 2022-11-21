from abc import ABCMeta, abstractmethod


class AbstractFilter(metaclass=ABCMeta):
    '''
    筛选form data的抽象类
    '''

    @abstractmethod
    def filter(self, data: dict):
        pass