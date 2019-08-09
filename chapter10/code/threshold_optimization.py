"""获取最佳阈值"""
import pandas as pd
import numpy as np

infile = "../data/water_heater.xls"
data = pd.read_excel(infile)
data = data[data['水流量'] > 0]
data['发生时间'] = pd.to_datetime(data['发生时间'], format="%Y%m%d%H%M%S")

def get_event(ts):
    tmp = data["发生时间"].diff() > ts
    return tmp.sum() + 1

def get_threshold():
    n = 4
    threshold = pd.Timedelta(minutes=5)
    list_ts = [pd.Timedelta(minutes=i) for i in np.arange(1, 9, 0.25)]
    tmp = pd.DataFrame(list_ts, columns=["阈值"])
    tmp['事件数'] = tmp["阈值"].apply(get_event)
    tmp['斜率'] = abs(tmp['事件数'].diff()) / 0.25
    tmp['斜率指标'] = tmp['斜率'].rolling(n).mean()
    ts = tmp['阈值'][tmp['斜率指标'].idxmin() - n]
    if ts > threshold:
        ts = pd.Timedelta(minutes=4)
    print(ts)




if __name__ == '__main__':
    get_threshold()
    pass