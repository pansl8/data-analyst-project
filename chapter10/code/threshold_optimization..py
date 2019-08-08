# -*- coding:utf-8 -*-
import pandas as pd
import numpy as np

infile = "../data/water_heater.xls"
data = pd.read_excel(infile)
data = data[data['水流量'] > 0]
data['发生时间'] = pd.to_datetime(data['发生时间'], format='%Y%m%d%H%M%S')
# 专家阈值
threshold = pd.Timedelta(minutes=5)

def event_num(ts):
    """
    根据给定的时间阈值，返回事件数
    :param ts: 时间阈值
    :return: 事件数
    """
    tmp = data['发生时间'].diff() > ts
    return tmp.sum() + 1

# 构造时间阈值序列
dt = [pd.Timedelta(minutes=i) for i in np.arange(1, 9, 0.25)]
print(len(dt))
h = pd.DataFrame(dt, columns=['阈值'])
temp = h['阈值'].apply(event_num)
print(temp)