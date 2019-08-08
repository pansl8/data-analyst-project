# -*- coding:utf-8 -*-
"""用k_means对数据进行聚类分析"""
import pandas as pd
from sklearn.cluster import  KMeans

def cluster():
    file = "../tmp/zscoreddata.xls"
    data = pd.read_excel(file)

    kmodel = KMeans(n_clusters=5, n_jobs=4)
    kmodel.fit(data)
    r1 = pd.Series(kmodel.labels_).value_counts()
    r2 = pd.DataFrame(kmodel.cluster_centers_)
    r = pd.concat([r2, r1], axis=1)
    r.columns = list(data.columns) + ['cluster_counts']
    print(r)

if __name__ == '__main__':
    cluster()