# -*- coding: utf-8 -*-

"""
regression analysis of NAROU data
recuring "fav_novel_cnt" of NAROU data
input: NAROU csv data header:["fav_novel_cnt","length","all_point","general_all_no","review_cnt","kaiwaritu"]
i will add tf-idf value of story and tf-idf value of keyword
"""

import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

from sklearn.svm import SVR

def main():
    f = sys.argv[1]
    ft = sys.argv[2]
    df = pd.read_csv(f)
    dft = pd.read_csv(ft)
    
    X = df[["length","all_point","general_all_no","review_cnt","kaiwaritu"]]
    y = df["fav_novel_cnt"]
    print("1")

    test_X = dft[["length","all_point","general_all_no","review_cnt","kaiwaritu"]]
    test_y = dft["fav_novel_cnt"]
    print("2")

    svr_lin = SVR(kernel="linear")
    print("3")

    #y_lin = svr_lin.fit(X, y).predict(X)
    svr_lin.fit(X, y)
    print("4")

    test_lin = svr_lin.predict(test_X)
    print("5")

    print("予測:", test_lin)
    print("正解:", test_y)

if __name__ == "__main__":
    main()