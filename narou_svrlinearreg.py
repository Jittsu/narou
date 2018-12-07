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

def main():
    f = sys.argv[1]
    df = pd.read_csv(f)
    X = df.iloc[:, 2:]
    X = sparse.csr_matrix(X.to_sparse(), dtype=np.float32)
    Y = df.iloc[:, 1].values
    Y = np.log(Y+1).astype(np.float32)
    #print(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

    svr_lin = SVR(kernel="rbf", C=1e-1, gamma=1e-10)
    y_lin = svr_lin.fit(X_train, Y_train).predict(X_train)

    Y_pred = svr_lin.predict(X_test)

    corr = np.corrcoef(Y_test, Y_pred)[0, 1]
    #lin_RMS = sqrt(mean_squared_error(Y_test, test_lin))
    RMSPE = (np.sqrt(np.mean(((Y_test-Y_pred) / (Y_test+1)) ** 2)))
    R2_SCORE = r2_score(Y_test, Y_pred)

    print("rbf: RMSPE %f \t Corr %f \t R2_SCORE %f" % (RMSPE, corr, R2_SCORE))

    plt.title("C=%s, gamma=%s" % (str(svr_lin.C), str(svr_lin.gamma)))
    plt.xlabel("Y_test")
    plt.ylabel("Y_pred")
    plt.scatter(Y_test, Y_pred)
    plt.plot(Y_test, Y_test, color="r")
    plt.show()
    


if __name__ == "__main__":
    main()