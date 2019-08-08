from keras.models import Sequential
from keras.layers.core import Dense, Activation
import pandas as pd
from cm_plot import *


def lm_fit():
    file = "../data/model.xls"
    net_file = "../tmp/model.xls"
    data = pd.read_excel(file)
    data = data.as_matrix()
    p = 0.8
    train = data[:int(len(data) * p), :]
    test = data[int(len(data) * p):, :]

    net = Sequential()
    net.add(Dense(input_dim=3, units=10))
    net.add(Activation('relu'))
    net.add(Dense(input_dim=10, units=1))
    net.add(Activation('sigmoid'))
    net.compile(loss='binary_crossentropy', optimizer='adam',
                sample_weight_mode='binary')
    net.fit(train[:, :3], train[:, 3], nb_epoch=1000, batch_size=1)
    net.save_weights(net_file)
    predict_result = net.predict_classes(train[:,:3]).reshape(len(train))
    cm_plot(train[:, 3], predict_result).show()


if __name__ == '__main__':
    lm_fit()
