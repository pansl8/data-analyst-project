# -*- coding:utf-8 -*-
import pandas as pd


def standard_data():
    inflie = "../data/zscoredata.xls"
    outfile = "../tmp/zscoreddata.xls"
    data = pd.read_excel(inflie)
    data = (data - data.mean(axis=0)) / data.std(axis=0)
    data.columns = ['Z' + i for i in data.columns]
    data.to_excel(outfile, index=False)


if __name__ == '__main__':
    standard_data()
