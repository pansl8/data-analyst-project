"""模型检验"""
import pandas as pd

def check():
    infile = '../data/predictdata.xls'
    data = pd.read_excel(infile)
    abs_ = (data['预测值'] - data['实际值']).abs()
    mae = abs_.mean()
    rmse = (abs_**2).mean() ** 0.5
    mape = (abs_/data['实际值']).mean()
    print(mae, rmse, mape)


if __name__ == '__main__':
    check()