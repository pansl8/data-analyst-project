# -*- coding:utf-8 -*-
"""自定义apriori算法模块"""
import pandas as pd

# 自定义连接函数
def connect_string(x, ms):
    x = list(map(lambda i: sorted(i.split(ms)), x))
    r = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i][:-1] == x[j][:-1] and x[i][-1] != x[j][-1]:
                r.append(x[i][:-1] + sorted([x[j][-1], x[i][-1]]))
    return r


# 寻找关联规则函数
def find_rule(d, support, confidence, ms=u"--"):
    result = pd.DataFrame(index=["support", "confidence"])

    # 第一批支持度筛选
    support_series = 1.0 * d.sum() / len(d)

    column = list(support_series[support_series > support].index)
    k = 0

    while len(column) > 1:
        k = k + 1
        print(u"\n正在进行第%s次搜索..." % k)

        column = connect_string(column, ms)
        print(u"数目%s..." % len(column))
        index_lst = [ms.join(i) for i in column]

        # 新的支持度函数
        sf = lambda i: d[i].prod(axis=1, numeric_only=True)
        # 计算连接后的支持度，开始筛选
        d_2 = pd.DataFrame(list(map(sf, column)), index=index_lst).T
        support_series_2 = 1.0 * d_2[index_lst].sum() / len(d)
        column = list(support_series_2[support_series_2 > support].index)

        support_series = support_series.append(support_series_2)
        column2 = []
        # 遍历所有可能的情况
        for i in column:
            i = i.split(ms)
            for j in range(len(i)):
                column2.append(i[:j] + i[j + 1:] + i[j:j + 1])

        # 置信度序列
        cofidence_series = pd.Series(index=[ms.join(i) for i in column2])

        for i in column2:
            cofidence_series[ms.join(i)] = support_series[ms.join(
                sorted(i))] / support_series[ms.join(i[:-1])]
        # 置信度筛选
        for i in cofidence_series[cofidence_series > confidence].index:
            result[i] = 0.0
            result[i]["confidence"] = cofidence_series[i]
            result[i]["support"] = support_series[ms.join(sorted(i.split(ms)))]

    result = result.T.sort_values(["confidence", "support"], ascending=False)
    print(u"\nresult:")
    print(result)

    return result