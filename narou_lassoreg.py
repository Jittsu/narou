# -*-coding: utf-8 -*-

"""
using csv data in mge:/mnt/hdd1/data/narou/genre_reg/
"""


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from scipy import sparse

f = sys.argv[1]
df = pd.read_csv(f)
X = df.iloc[:, 2:]
X = sparse.csr_matrix(X.to_sparse(), dtype=np.float32)
Y = df.iloc[:, 1].values
Y = np.log(Y+1).astype(np.float32)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

clf = Lasso(alpha=1.0)
clf.fit(X_train, Y_train)

Y_pred = clf.predict(X_test)
corr = np.corrcoef(Y_test, Y_pred)[0, 1]
RMSPE = (np.sqrt(np.mean(((Y_test-Y_pred) / (Y_test+1)) ** 2)))
print("Lasso: RMSPE %f \t Corr %f" % (RMSPE, corr))

#plt.plot(Y_pred, linestyle="solid", label="lasso")
#plt.plot(X_test, Y_pred, "r-")
#plt.plot(X_test, Y_test, "o")
#plt.scatter(Y_pred, Y_test, color="b")
#plt.plot(clf.predict(X_train), "r-", color="r")
plt.scatter(Y_test, Y_pred, color="b")
plt.plot(Y_test, Y_test, color="r")
plt.show()