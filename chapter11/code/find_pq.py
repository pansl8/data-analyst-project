"""找出arima（p, d, q）模型最适合的参数"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

def get_pq():
    '''返回最佳p, q值'''
    infile = "../data/discdata_processed.xls"
    data = pd.read_excel(infile)
    data = data.iloc[:len(data) - 5]
    xdata = data['CWXT_DB:184:D:\\']
    pmax = qmax = int(len(xdata) / 10)
    bic_matrix = []
    for p in range(pmax + 1):
        tmp =[]
        for q in range(qmax + 1):
            try:
                tmp.append(ARIMA(xdata, (1, 1, 1)).fit().bic)
            except Exception:
                tmp.append(None)
        bic_matrix.append(tmp)
    p, q = pd.DataFrame(bic_matrix).stack().idxmin()
    return p, q


if __name__ == '__main__':


    pass