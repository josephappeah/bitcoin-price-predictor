import quandl
import numpy as np


def get_data(feature, days):
    # Retrieve Data
    quandl.ApiConfig.api_key = 'qinG5wphqPidgvqrpbPW'

    data = quandl.get(feature, returns="numpy")
    data = data[-days:]
    m = int(data.shape[0])  # num of samples


    train_Y = np.empty([m, 1])
    train_X = np.arange(0, m)

    i = 0
    for y in data:
        train_Y[i] = y[1]
        i += 1

    return train_X.reshape((m,)), train_Y.reshape((m, ))