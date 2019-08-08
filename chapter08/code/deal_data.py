# -*- coding:utf-8 -*-
"""数据预处理:采用KMeans算法对数据进行聚类处理并保存"""
import pandas as pd
from sklearn.cluster import KMeans

infile = "../data/data.xls"
outfile = "../tmp/data_processed.xls"

data = pd.read_excel(infile)
typelabel = {
    "肝气郁结证型系数": "A",
    "热毒蕴结证型系数": "B",
    "冲任失调证型系数": "C",
    "气血两虚证型系数": "D",
    "脾胃虚弱证型系数": "E",
    "肝肾阴虚证型系数": "F",
}
keys = list(typelabel.keys())
k = 4
result = pd.DataFrame()

# for i in range(len(typelabel)):
kmodel = KMeans(n_clusters=k, n_jobs=4)
kmodel.fit(data[keys[0]].as_matrix())
# r1 = pd.DataFrame(kmodel.cluster_cen
# ters_, columns=[typelabel[keys[0]]])
# r2 = pd.Series(kmodel.labels_).value_counts()
# r = pd.concat([r1, r2])
# print(r)