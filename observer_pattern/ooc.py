from db_connect import Model
from observer_pattern import Observable


class OOC(Observable):
    point: float
    model: Model

    def __init__(self, lcl: float, ucl: float):
        super(OOC, self).__init__()
        self.lcl = lcl
        self.ucl = ucl

    def get_point(self) -> float:
        return self.point

    def set_point(self, i: int, point: float):
        self.point = point
        print(f'i:{i},lcl:{self.lcl},point:{self.point},ucl:{self.ucl}')
        self.notify()

    def set_model(self, model: Model):
        self.model = model
        print(f' lcl:{self.lcl},point:{model.data},ucl:{self.ucl}')
        self.notify()