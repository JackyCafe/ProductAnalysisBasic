''' 
2023/3/22
ProductAnalysisBasic 
operator_mode.py
by yhlin
'''
from db_connect import Model
from observer_pattern import Subject


class OperatorMode(Subject):
    _model: Model

    def __init__(self):
        super(OperatorMode, self).__init__()

    @property
    def point(self) -> float: return self._point

    @point.setter
    def point(self, point):
        self._point = point
        self.notify_all()

    @property
    def model(self) -> Model: return self._model

    @model.setter
    def model(self, model: Model):
        self._model = model
        self.notify_all()
