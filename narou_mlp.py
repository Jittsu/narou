# -*- coding: utf-8 -*-

"""
regression analysis of NAROU data
recuring "fav_novel_cnt" of NAROU data
input: NAROU csv data header:["fav_novel_cnt","length","all_point","general_all_no","review_cnt","kaiwaritu"]
MLP
"""

import numpy as np
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.optimizers import Adam
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from math import sqrt
from scipy import sparse
from statistics import mean, mode, pvariance

def main():
    f = sys.argv[1]
    df = pd.read_pickle(f)
    X = df[:, 1:]
    Y = df[:, 0].todense()
    Y = pd.DataFrame(Y)
    Y = Y.iloc[:, 0].values
    Y = np.log(Y+1).astype(np.float64)
    m = mean(Y)
    p = pvariance(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    keras = KerasRegressor(build_fn=model, epochs=300, batch_size=128, verbose=0)
    keras.fit(X_train, Y_train)

    predicted = keras.predict(X_test)

    corr = np.corrcoef(Y_test, predicted)[0, 1]
    RMSPE = (np.sqrt(np.mean(((Y_test-predicted) / (Y_test+1)) ** 2)))
    r2 = r2_score(Y_test, predicted)
    print("Corr:%f, RMSPE:%f, R2_SCORE:%f\n" % (corr, RMSPE, r2))

    plt.title("Corr:%s, RMSPE:%s, R2_SCORE:%s" % (corr, RMSPE, r2))
    plt.xlabel("Y_test", fontsize=20)
    plt.ylabel("Y_pred", fontsize=20)
    plt.grid(which="both")
    plt.scatter(Y_test, predicted, marker='.', s=50)
    plt.plot(Y_test, Y_test, color="r")
    plt.axhline(y=m, color="green")
    plt.tick_params(labelsize=20)
    plt.show()

def model():
    model = Sequential()
    model.add(Dense(1200, input_shape=(1309,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(800))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(400))
    model.add(Activation('relu'))
    model.add(Dense(100))
    model.add(Activation('relu'))
    model.add(Dense(10))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

if __name__ == "__main__":
    main()
