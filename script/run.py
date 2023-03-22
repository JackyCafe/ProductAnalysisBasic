from db_connect.queryDb import QueryDb
import numpy as np
import matplotlib.pyplot as plt

from db_connect.spc import SPC
from observer_pattern import CheckSpc, OperatorMode


def main():
    show_spc()


def show_spc():
    q = QueryDb()
    q.read_csv('product.csv')
    params = q.cols[4]
    value = [model.data for model in q.get(params)]
    data = np.array(value, dtype='float')
    spc = SPC(data)
    x_bar = spc.x_bar
    ucl = spc.ucl
    lcl = spc.lcl
    spc.to_chart()



if __name__ == '__main__':
    main()