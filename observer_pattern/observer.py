import abc


class Observer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, subject, object_id=0):
        pass
