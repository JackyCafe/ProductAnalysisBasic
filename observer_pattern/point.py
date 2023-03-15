from db_connect.queryDb import QueryDb
from observer_pattern import Observer, OOC


class Point(Observer):
    def update(self, observable, object_id=0):
        if isinstance(observable, OOC):
            point = float(observable.model.data)

            if point > observable.ucl or point < observable.lcl:
                q = QueryDb()
                q.update(observable.model.id, 1)
                print(f"OOC:{observable.model._id}")