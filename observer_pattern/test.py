''' 
2023/3/22
ProductAnalysisBasic 
test.py
by yhlin
'''
import numpy as np

from db_connect.queryDb import QueryDb
from db_connect.spc import SPC
from observer_pattern import CheckSpc, OperatorMode


def main():
    q = QueryDb()
    ids=[]
    cols = list(q.cols)
    col = cols[5]
    models = q.get(col)
    datas = []
    for i, model in enumerate(models):
        ids.append(model._id)
        datas.append(model.data)
    values = np.array(datas, dtype=float)
    spc = SPC(values)
    x_bar = spc.x_bar
    ucl = spc.ucl[0]  # 上管制界線
    lcl = spc.lcl[0]  # 下管制界線
    cks = CheckSpc(ucl, lcl)
    operatorMode = OperatorMode()
    operatorMode.add_observer(cks)
    for model in models:
        operatorMode.model = model



if __name__ == '__main__':
    main()