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

def main():
    f = sys.argv[1]
    n = sys.argv[2]
    columns = ["ncode","fav_novel_cnt","kaiwaritu","length","review_cnt","userid"]
    culc_columns = ["general_all_no","general_firstup","general_lastup"]

    df1 = pd.read_csv(f)
    df2 = df1[columns]
    df2.userid = df2.userid.apply(lambda x:str(x))
    df3 = pd.get_dummies(df2,columns=["userid"])

    cdf1 = df1[culc_columns]
    cdf1.general_firstup = cdf1.general_lastup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) - cdf1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    cdf1.general_firstup = cdf1.general_firstup.apply(lambda x:x.total_seconds()).apply(lambda x:86400 if x<86400 else x)
    cdf2 = pd.DataFrame()
    cdf2["weekup_ave"] = cdf1.general_firstup
    cdf2.weekup_ave = cdf2.weekup_ave.apply(lambda x: x/86400)
    #print(cdf2)
    #print(cdf1.general_all_no)
    cdf2.weekup_ave = cdf1.general_all_no / cdf2.weekup_ave
    #print(cdf2)

    df = pd.concat([df3, cdf2], axis=1)
    #print(df)

    #outdf = sparse.csr_matrix(df3.to_sparse(), dtype=np.float32)
    df.to_csv("{0}.csv".format(n), index= False)
    #mmwrite("{0}".format(n), outdf)

    #print(df)


if __name__ == "__main__":
    main()