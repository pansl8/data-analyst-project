"""平稳性检验"""
import pandas as pd
from statsmodels.tsa.stattools import adfuller as ADF

def get_adf():
    infile = "../data/discdata_processed.xls"
    data = pd.read_excel(infile)
    data = data.iloc[:len(data) - 5]
    adf = ADF(data["CWXT_DB:184:D:\\"])
    diff = 0
    while adf[1] > 0.05:
        diff += 1
        adf = ADF(data["CWXT_DB:184:D:\\"].diff(diff).dropna())

    print("经过%d阶差分后归于平稳,p值为%s" % (diff, adf[1]))


if __name__ == '__main__':
    get_adf()