''' 
2023/3/22
ProductAnalysisBasic 
check_spc.py
by yhlin
'''
from db_connect.queryDb import QueryDb
from observer_pattern import Observer, OperatorMode


class CheckSpc(Observer):
    def __init__(self, ucl: float, lcl: float):
        self.ucl = ucl
        self.lcl = lcl

    def update(self, subject, object_id=0):
        point = float(subject.model.data)

        if isinstance(subject, OperatorMode):
            print(f'{point} out of spec ({self.ucl},{self.lcl})')

            if point > self.ucl or point < self.lcl:
                q = QueryDb()
                print(subject.model.id)
                q.update(subject.model._id,1)
                print(f'{point} out of spec ({self.ucl},{self.lcl})')
