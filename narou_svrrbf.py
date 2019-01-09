# -*- coding: utf-8 -*-

"""
regression analysis of NAROU data
recuring "fav_novel_cnt" of NAROU data
input: NAROU csv data header:["fav_novel_cnt","length","all_point","general_all_no","review_cnt","kaiwaritu"]
"""

import numpy as np
import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from math import sqrt
from scipy import sparse
from sklearn.model_selection import GridSearchCV

def main():
    tuned_parameters = {'C': [0.01,0.1,1,10,100,1000], 'kernel': ["rbf"], 'gamma': [0.01,0.001,0.0001,0.00001]}
    clf = GridSearchCV(SVR(), tuned_parameters, cv=5, scoring="r2", n_jobs=10)
    """
    f = sys.argv[1]
    df = pd.read_csv(f)
    X = df.iloc[:, 2:]
    X = sparse.csr_matrix(X.to_sparse(), dtype=np.float32)
    Y = df.iloc[:, 1].values
    Y = np.log(Y+1).astype(np.float32)
    #print(X)
    """
    f = sys.argv[1]
    df = pd.read_pickle(f)
    X = df[:, 1:]
    Y = df[:, 0].todense()
    Y = pd.DataFrame(Y)
    Y = Y.iloc[:, 0].values
    Y = np.log(Y+1).astype(np.float32)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    #svr_lin = SVR(kernel="rbf", C=10, gamma=1e-5)
    #y_lin = svr_lin.fit(X_train, Y_train).predict(X_train)
    clf.fit(X_train, Y_train)
    Y_pred = clf.predict(X_test)

    #Y_pred = svr_lin.predict(X_test)

    corr = np.corrcoef(Y_test, Y_pred)[0, 1]
    RMSPE = (np.sqrt(np.mean(((Y_test-Y_pred) / (Y_test+1)) ** 2)))
    print("Corr:%f, RMSPE:%f, R2_SCORE:%f\n%s" % (corr,RMSPE,clf.best_score_,clf.best_params_))

    plt.title("Coor:%s, RMSPE:%s, R2_SCORE:%s, %s" % (corr,RMSPE,clf.best_score_,clf.best_params_))
    plt.xlabel("Y_test")
    plt.ylabel("Y_pred")
    plt.scatter(Y_test, Y_pred)
    plt.plot(Y_test, Y_test, color="r")
    plt.show()

    """
    corr = np.corrcoef(Y_test, Y_pred)[0, 1]
    RMSPE = (np.sqrt(np.mean(((Y_test-Y_pred) / (Y_test+1)) ** 2)))
    R2_SCORE = r2_score(Y_test, Y_pred)

    print("rbf: RMSPE %f \t Corr %f \t R2_SCORE %f" % (RMSPE, corr, R2_SCORE))

    plt.title("C=%s, gamma=%s" % (str(svr_lin.C), str(svr_lin.gamma)))
    plt.xlabel("Y_test")
    plt.ylabel("Y_pred")
    plt.scatter(Y_test, Y_pred)
    plt.plot(Y_test, Y_test, color="r")
    plt.show()
    """


if __name__ == "__main__":
    main()