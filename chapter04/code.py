import pandas as pd
import numpy as np
from scipy.interpolate import lagrange
import os


def programmer01():
    input_file = "./data/catering_sale.xls"
    output_file = "./temp/sales.xls"

    data = pd.read_excel(input_file)
    data['销量'][(data['销量'] < 400) | (data['销量'] > 5000)] = None
    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:
                data[i][j] = ployinterp_columns(data[i], j)
    data.to_excel(output_file)


def ployinterp_columns(s, n, k=5):
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)


def programmer02():
    filename = './data/electricity_data.xls'
    output_file = './temp/electricity_data.xls'
    data = pd.read_excel(filename)
    data['线损率'] = (data['供入电量'] - data['供出电量']) / data['供入电量']
    print(data)
    data.to_excel(output_file, index=False)

if __name__ == "__main__":
    programmer02()
    