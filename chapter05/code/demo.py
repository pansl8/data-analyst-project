import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def k_means01():
    infile = '../data/consumption_data.xls'
    oufile = '../temp/data_type.xls'
    data = pd.read_excel(infile, index_col='Id')
    k = 3
    iteration = 500
    data_zs = 1.0 * (data - data.mean()) / data.std()
    model = KMeans(n_clusters=k, n_jobs=4, max_iter=iteration)
    model.fit(data_zs)
    r1 = pd.Series(model.labels_).value_counts()
    r2 = pd.DataFrame(model.cluster_centers_)
    r = pd.concat([r2, r1], axis=1)
    r.columns = list(data.columns) + ['类别数目']
    # print(r)

    r = pd.concat([data, pd.Series(model.labels_, index=data.index)], axis=1)
    r.columns = list(data) + ['聚类类别']
    # print(r)
    r.to_excel(oufile)
    for i in range(k):
        density_plot02(data[r['聚类类别'] == i], k).savefig('%s%s.png' % (oufile, i))


def density_plot(data, title):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure()
    for i in range(len(data.iloc[0])):
        data.iloc[:, i].plot(kind='kde', label=data.columns[i], linewidth=2)
    plt.ylabel('密度')
    plt.xlabel('人数')
    plt.title('聚类类别%s各属性的密度曲线' % title)
    plt.legend()
    return plt


def density_plot02(data, k):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    p = data.plot(kind='kde', linewidth=2, subplots=True, sharex=False)
    [p[i].set_ylabel('密度') for i in range(k)]
    plt.legend()
    return plt


if __name__ == "__main__":
    k_means01()
