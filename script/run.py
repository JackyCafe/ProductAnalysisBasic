from db_connect.queryDb import QueryDb
import numpy as np
import matplotlib.pyplot as plt

from db_connect.spc import SPC
from observer_pattern import OOC
from observer_pattern.point import Point


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
    models = q.get(params)
    datas = []
    ids = []

    for i, model in enumerate(models):
        ids.append(model._id)
        datas.append(model.data)
    '''observer'''
    ooc = OOC(lcl, ucl)
    point = Point()
    ooc.add_observer(point)
    for model in models:
        ooc.set_model(model)

    fig, axs = plt.subplots(1, figsize=(15, 15), sharex=True)
    axs.plot(x_bar, marker='o', color='black')
    axs.plot(ucl, linestyle='dashed', marker='o', color='red')
    axs.plot(lcl, linestyle='dashed', marker='o', color='red')
    axs.plot(data, linestyle='-', marker='o', color='blue')
    plt.show()


if __name__ == '__main__':
    main()