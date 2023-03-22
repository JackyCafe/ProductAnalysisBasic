''' 
2023/3/22
ProductAnalysisBasic 
subject.py
by yhlin
'''


class Subject:

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_all(self):
        for o in self.observers:
            o.update(self)
