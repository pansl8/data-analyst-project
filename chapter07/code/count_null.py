# -*- coding:utf-8 -*-
import pandas as pd

def count_null():
    infile = "../data/air_data.csv"
    outfile = "../tmp/explore.xls"
    clearnedflie = "../tmp/data_clearned.csv"
    data = pd.read_csv(infile, encoding="utf-8")

    # 统计每个字段缺失值的数量
    explore = data.describe(percentiles=[], include="all").T
    explore["null"] = len(data) - explore["count"]
    explore = explore[["max", "min", "null"]]
    explore.to_excel(outfile)

    # 数据预处理，丢弃票价为空的数据
    data1 = data[data["SUM_YR_1"].notnull() * data["SUM_YR_2"].notnull()]
    index1 = data1["SUM_YR_1"] != 0
    index2 = data1["SUM_YR_2"] != 0
    index3 = (data1["SEG_KM_SUM"] == 0) & (data1["avg_discount"] == 0)
    data2 = data1[index1 | index2 | index3]
    data2.to_csv(clearnedflie)

if __name__ == '__main__':
    count_null()