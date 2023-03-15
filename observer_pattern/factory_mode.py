from observer_pattern import Subject


class FactoryMode(Subject):
    def __init__(self, point: float):
        super(FactoryMode, self).__init__()
        self._point = point

    @property
    def point(self) -> float: return self._point

    @point.setter
    def point(self, point):
        self._point = point
        self.notify_all()