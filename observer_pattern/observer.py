import abc

'''如果希望子類別在被繼承後一定要實作的方法，可以在父類別中指定metaclass 
為abc 模組的ABCMeta，並在指定方法中加上註記為abc 模組的@abstractmethod '''


class Observer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self, observable, object_id=0):
        pass
