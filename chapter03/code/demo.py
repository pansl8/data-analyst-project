import pandas as pd
# from statsmodels.tsa.stattools import adfuller as ADF 
# ADF平稳性检验
import numpy as np 
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn import svm

s = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print(s)
d = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'c'])
print(d)
print(np.random.randint(100))
model = LinearRegression()
print(model)

iris = datasets.load_iris()
clf = svm.LinearSVC()
clf.fit(iris.data, iris.target)
clf.predict([[5.0, 3.6, 1.3, 0.25]])
print(clf.coef_)