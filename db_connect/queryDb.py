from db_connect import CreateDB, Model
import pandas as pd


class QueryDb(CreateDB):

    def __init__(self):
        super().__init__()
        self._datas = self.find(**{})

    @property
    def datas(self):
        return list(self._datas)

    '''@property
    def cols(self, index=1):
        return list(self._cols)'''

    @property
    def id(self):
        datas = self.collection.find({}, {'_id': 1})
        return [f'{data.get("_id")}' for num, data in enumerate(datas, start=1)]

    def to_df(self):
        '''將colllection 的資料轉成df'''
        df = pd.DataFrame(list(self.collection.find({})))
        return df

    def update(self, id: str, value: int):
        self.collection.update_one({"_id": id}, {"$set": {"NG": value}})

    def get(self, param: str) -> list:
        id = []
        result = []
        cursors = self.collection.find({}, {param})

        for cursor in cursors:
            id = cursor['_id']
            data = cursor[param]
            model = Model(id, data)
            result.append(model)
        return result

    def mean(self, param: str) -> float:
        result = self.get(param)
        sum: float = 0.0
        count: int = len(result.get(param))
        for x in result.get(param):
            sum += float(x)
        return sum / count



    def __getitem__(self, position) -> dict:
        return self.datas[position]


if __name__ == '__main__':
    spc = QueryDb()
    spc.read_csv('product.csv')
    try:
        spc.insert()
    except BaseException as be:
        print(be)
    print(spc.id)
