"""arima模型预测"""
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox

def arima_predict():
    infile = '../data/discdata_processed.xls'
    data = pd.read_excel(infile, index_col="COLLECTTIME")
    lagnum = 12
    data = data.iloc[:len(data)-5]

    xdata = data['CWXT_DB:184:D:\\']
    arima = ARIMA(xdata, (0, 1, 1)).fit()
    predict = arima.predict(typ="levels")
    pred_error = (predict - xdata).dropna()

    b, p = acorr_ljungbox(pred_error, lags=lagnum)
    h = (p < 0.05).sum()
    print(h)
    if h > 0:
        print("arima(0, 1, 1)不符合白噪声检验")
    else:
        print("arima(0, 1, 1)符合白噪声检验")


if __name__ == '__main__':
    arima_predict()
