from observer_pattern import Observer, FactoryMode, Subject


class CheckSpec(Observer):
    ucl: float
    lcl: float

    def __init__(self, ucl: float, lcl: float):
        self.ucl = ucl
        self.lcl = lcl

    def update(self, fm:FactoryMode, object_id=0):
        if isinstance(fm,FactoryMode):
            point = float(fm.point)

            if point>self.ucl or point< self.lcl:
                print(f'{point} out of spec ({self.ucl},{self.lcl})' )
            else:
                print(f'{point} in  spec ({self.ucl},{self.lcl})' )
