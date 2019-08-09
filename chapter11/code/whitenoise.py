"""检验白噪声"""

import pandas as pd
from statsmodels.stats.diagnostic import acorr_ljungbox


def is_whitenoise():
    infile = "../data/discdata_processed.xls"
    data = pd.read_excel(infile)
    data = data.iloc[:len(data) - 5]

    b, p = acorr_ljungbox(data["CWXT_DB:184:D:\\"].dropna(), lags=1)
    if p < 0.05:
        print("给定数据不是白噪声序列p:", p[0])
    else:
        print("给定数据是白噪声序列p:", p[0])

    b, p = acorr_ljungbox(data["CWXT_DB:184:D:\\"].diff().dropna(), lags=1)
    if p < 0.05:
        print("给定数据的一阶差分不是白噪声序列p:", p[0])
    else:
        print("给定数据的一阶差分是白噪声序列p:", p[0])
    print(b[0])


if __name__ == '__main__':
    is_whitenoise()
