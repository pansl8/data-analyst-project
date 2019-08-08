import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def programmer01(filename):
	"""绘制箱型图"""
	data = pd.read_excel(filename, index_col=u'日期')
	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False

	plt.figure()
	p = data.boxplot(return_type='dict')
	x = p['fliers'][0].get_xdata()  # fliers为异常值的标签
	y = p['fliers'][0].get_ydata()
	y.sort()

	for i in range(len(x)):
		if i > 0:
			plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.5 -0.8 / 
    			(y[i] - y[i - 1]), y[i]))
		else:
			plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.8, y[i]))
			plt.show()

def programmer02(file_name):
	"""导入数据，获取极差， 变异系数， 四分位间距"""
	data = pd.read_excel(file_name, index_col=u'日期')
	data = data[(data['销量'] > 400) & (data['销量'] < 5000)]
	statistics = data.describe()
	print(statistics)

	statistics.loc['range'] = statistics.loc['max'] - statistics.loc['min']
	statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
	statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']
	print(statistics)

def programmer03(file_name):
	data = pd.read_excel(file_name, index_col='菜品名')
	data = data['盈利'].copy()
	data.sort_values(ascending=False)

	plt.rcParams['font.sans-serif'] = ['SimHei']
	plt.rcParams['axes.unicode_minus'] = False
	plt.figure()

	data.plot(kind='bar')
	plt.ylabel('盈利（元）')
	p = 1.0 * data.cumsum() / data.sum()
	p.plot(color='r', secondary_y=True, style='-o', linewidth=2)
	plt.annotate(format(p[6], '.4%'), xy=(6, p[6]), xytext=(6*0.9, p[6]*0.9), 
		arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
	plt.ylabel('盈利（比例）')
	plt.show()





if __name__ == '__main__':
    file_name = "../data/catering_sale.xls"
    file_name03 = "../data/catering_dish_profit.xls"
    programmer03(file_name03)
 
