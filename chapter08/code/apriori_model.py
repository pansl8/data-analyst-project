# -*- coding:utf-8 -*-
"""建立apriori模型，获取关联规则"""
import pandas as pd
from apriori import find_rule
import time

def run():
    file = "../data/apriori.txt"
    data = pd.read_csv(file, header=None, dtype=object)
    start = time.clock()
    print("开始转换为0-1矩阵")
    ct = lambda x : pd.Series(1, index=x[pd.notnull(x)])
    tmp = list(map(ct, data.as_matrix()))
    data = pd.DataFrame(tmp).fillna(0)
    end = time.clock()
    print("转换结束， 用时：", (end - start))
    del tmp

    support = 0.06
    confidence = 0.75
    ms = "---"
    start = time.clock()
    print("开始搜索关联规则...")
    find_rule(data, support, confidence, ms=ms)
    end = time.clock()
    print("\n搜索完成，用时%.2f秒：" % (end - start))

if __name__ == '__main__':
    run()