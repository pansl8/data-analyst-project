# -*- coding:utf-8 -*-
import pandas as pd

def train_test():
    infile = "data/moment.csv"
    cm_test = "tmp/cm_test.xls"
    cm_train = "tmp/cm_train.xls"
    data = pd.read_csv(infile, encoding="GBK")
    print(data)

if __name__ == '__main__':
    train_test()