# -*- coding: utf-8 -*-

"""
regression analysis of NAROU data
recuring "fav_novel_cnt" of NAROU data
input: NAROU csv data header:["fav_novel_cnt","length","all_point","general_all_no","review_cnt","kaiwaritu"]
Ridge LINEAR
"""

import numpy as np
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from math import sqrt
from scipy import sparse
from sklearn.model_selection import GridSearchCV

def main():
    tuned_parameters = {'alpha': [0.01,0.1,1,10,100,1000]}
    clf = GridSearchCV(Lasso(), tuned_parameters, cv=5, scoring="r2", n_jobs=10)
    f = sys.argv[1]
    df = pd.read_pickle(f)
    X = df[:, 1:]
    Y = df[:, 0].todense()
    Y = pd.DataFrame(Y)
    Y = Y.iloc[:, 0].values
    Y = np.log(Y+1).astype(np.float32)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)

    corr = np.corrcoef(Y_test, Y_pred)[0, 1]
    RMSPE = (np.sqrt(np.mean(((Y_test-Y_pred) / (Y_test+1)) ** 2)))
    print("Corr:%f, RMSPE:%f, R2_SCORE:%f\n%s" % (corr,RMSPE,clf.best_score_,clf.best_params_))

    plt.title("Coor:%s, RMSPE:%s, R2_SCORE:%s, %s" % (corr,RMSPE,clf.best_score_,clf.best_params_))
    plt.xlabel("Y_test")
    plt.ylabel("Y_pred")
    plt.scatter(Y_test, Y_pred)
    plt.plot(Y_test, Y_test, color="r")
    plt.show()

if __name__ == "__main__":
    main()
