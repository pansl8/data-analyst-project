# -*- coding:utf-8 -*-
"""划分完整的一次用水事件"""
import pandas as pd

infile  = "../data/water_heater.xls"
outfile = "../tmp/dividsequence.xls"

data = pd.read_excel(infile)
data = data[data['水流量'] > 0]
data['发生时间'] = pd.to_datetime(data['发生时间'], format="%Y%m%d%H%M%S")
threshold = pd.Timedelta("4 min")
temp = data['发生时间'].diff() > threshold
data["事件编号"] = temp.cumsum() + 1
data.to_excel(outfile)