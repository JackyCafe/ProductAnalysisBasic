import math
import numpy as np
from matplotlib import  pyplot as plt
from db_connect.queryDb import QueryDb


class SPC:
    param: np.array
    x_bar: list = []
    _ucl: list = []
    _lcl: list = []
    _db : QueryDb

    def __init__(self, param: np.array):
        self.param = param
        count = self.param.shape[0]
        self.x_bar = np.repeat(self.mean, count)
        ucl = np.around(self.mean + 3*self.std,2)
        lcl = np.around(self.mean - 3 * self.std,2)

        self._ucl = np.repeat(ucl, count)
        self._lcl = np.repeat(lcl, count)

    @property
    def mean(self):
        return self.param.mean()

    @property
    def std(self):
        return self.param.std()

    @property
    def ucl(self) -> list:
        return self._ucl

    @property
    def lcl(self) -> list:
        return self._lcl

    def to_chart(self):
        fig, axs = plt.subplots(1, figsize=(15, 15), sharex=True)
        axs.plot(self._ucl, marker='o', color='red')
        axs.plot(self.x_bar, marker='o', color='black')
        axs.plot(self._lcl, marker='o', color='red')
        axs.plot(self.param,marker='_',color = 'blue')
        plt.show()


    def __len__(self):
        return len(self.param)