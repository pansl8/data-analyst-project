"""三层神经网络预测事件"""
import pandas as pd
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from cm_plot import cm_plot

def get_data():
    trainfile = "../data/train_neural_network_data.xls"
    testfile = "../data/test_neural_network_data.xls"
    train = pd.read_excel(trainfile).as_matrix()
    test = pd.read_excel(testfile).as_matrix()
    x_train = train[:, 5:]
    y_train = train[:, 4]
    x_test = test[:, 5:]
    y_test = test[:, 4]
    return x_train, y_train, x_test, y_test

def network_model():
    x_train, y_train, x_test, y_test = get_data()
    model = Sequential()
    model.add(Dense(input_dim=11, units=17))
    model.add(Activation('relu'))
    model.add(Dense(input_dim=17, units=10))
    model.add(Activation('relu'))
    model.add(Dense(input_dim=10, units=1))
    model.add(Activation('sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer='adam', sample_weight_mode='binary')
    model.fit(x_train, y_train, nb_epoch=100, batch_size=1)
    model.save_weights('../tmp/net.model')
    predict = model.predict_classes(x_test).reshape(len(x_test))
    print(predict)
    print(y_test)
    print(model.predict(x_test))
    cm_plot(y_test, predict)



if __name__ == '__main__':
    # network_model()
    pass