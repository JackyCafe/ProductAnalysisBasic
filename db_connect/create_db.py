'''
2023/3/14
product
db_connect.py
by yhlin
'''

import pandas as pd
from matplotlib.widgets import Cursor
from pandas import DataFrame, array
from pymongo import MongoClient


class CreateDB:
    df: DataFrame
    _clos: array
    record: dict

    def __init__(self ):
        self.clients = MongoClient()
        self.database = self.clients['product_db']
        self.collection = self.database['product_data']

    def read_csv(self, filename: str):
        self.df = pd.read_csv(filename)

        self.records = self.df.to_dict("records")

    @property
    def cols(self):
        return self.df.columns.array


    def insert(self):
        if len(self) > 0:
            raise BaseException("目前collection 已有資料，取消本次新增")
        else:
            self.collection.insert_many(self.records)

    def find(self, **kwargs):
        return self.collection.find(kwargs)

    def find_one(self, **kwargs):
        return self.collection.find_one(kwargs)

    def __len__(self):
        return self.collection.count_documents({})


def main():
    db = CreateDB()
    db.read_csv('product.csv')

    try:
        db.insert()
    except BaseException as be:
        print(be)

    params = {"工單編號": 19040103}
    params = {"工單編號": 19040103, "週期時間(秒)": {"$gt": 50}}
    # rows = db.find(**params)
    # for row in rows:
    #     print(row)

    # print(db.records)


if __name__ == '__main__':
    main()
