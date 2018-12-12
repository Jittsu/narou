# -*- coding: utf-8 -*-

"""
NAROU csv data preprocessing to select columns to .mtx or .csv
"""

import pandas as pd
import numpy as np
import sys
from scipy import sparse
from scipy.io import mmwrite, mmread
import datetime
from tfidfTransformer import pickle_transformer as pt

def main():
    f = sys.argv[1]
    n = sys.argv[2]
    columns = ["fav_novel_cnt","kaiwaritu","length","review_cnt","time","userid"]
    culc_columns = ["general_all_no","general_firstup","general_lastup"]

    df1 = pd.read_csv(f)
    df2 = df1[columns]
    df2.userid = df2.userid.apply(lambda x:str(x))
    df2.length = df2.length.apply(lambda x: x/100)
    df3 = pd.get_dummies(df2,columns=["userid"])

    cdf1 = df1[culc_columns]
    # general_lastupの値を1日毎の投稿頻度に ---
    cdf1.general_lastup = cdf1.general_lastup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) - cdf1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    cdf1.general_lastup = cdf1.general_lastup.apply(lambda x:x.total_seconds()).apply(lambda x:86400 if x<86400 else x).apply(lambda x: x/86400)
    # general_firstupの値をunix_timeに変更して週単位にする ---
    cdf1.general_firstup = cdf1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").timestamp()).apply(lambda x: x/604800)
    cdf2 = pd.DataFrame()
    cdf2[["general_all_no","firstup_unix","dayup_ave"]] = cdf1[["general_all_no","general_firstup","general_lastup"]]
    #cdf2.dayup_ave = cdf2.dayup_ave.apply(lambda x: x/86400)
    #print(cdf2)
    #print(cdf1.general_all_no)
    cdf2.dayup_ave = cdf2.general_all_no / cdf2.dayup_ave
    #print(cdf2)

    df = pd.concat([df3, cdf2], axis=1)

    #outdf = sparse.csr_matrix(df3.to_sparse(), dtype=np.float32)
    #df.to_csv("{0}.csv".format(n), index= False)
    #mmwrite("{0}".format(n), outdf)
    df = sparse.csr_matrix(df.to_sparse(), dtype=np.float32)
    save = pt(df)
    save.save_pkl(n)

    #print(df)


if __name__ == "__main__":
    main()