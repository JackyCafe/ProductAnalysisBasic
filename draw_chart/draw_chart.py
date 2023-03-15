import os

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['Taipei Sans TC Beta']

def PPA():
    df = pd.read_csv('../product.csv')
    keys = df.keys()
    params = keys.array
    paramsCount = len(params)
    var1 = df[params[4]]
    var2 = df[params[5]]
    params = {'param1': var1, 'param2': var2}
    to_draw(**params)


def to_draw(*args, **kwargs):
    p0_name = kwargs.get('param1').name
    p1_name = kwargs.get('param2').name
    p0 = np.array(kwargs.get('param1'))
    p1 = np.array(kwargs.get('param2'))
    coff = np.corrcoef(p0,p1)[0]
    fig, ax = plt.subplots()
    title = f'{p0_name} vs {p1_name} coff {coff}'
    plt.title(title)
    ax.scatter(p0, p1, s=10, c='red', marker='o', alpha=0.5, label=title)
    folderpath = f'{p0_name.replace("/", "_")}'

    if not os.path.isdir(folderpath):
        print(f"not created {folderpath}")

        os.makedirs(folderpath)
    plt.show()
    plt.savefig(f'{folderpath}\\{title}.png')
    plt.close(fig)


if __name__ == '__main__':
    PPA()