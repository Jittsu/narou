# -*- coding: utf-8 -*-

"""
NAROU csv data preprocessing to select columns to .pkl
using scale
"""

import pandas as pd
import numpy as np
import sys
from scipy import sparse
from scipy.io import mmwrite, mmread
import datetime
from tfidfTransformer import pickle_transformer as pt
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
mms = MinMaxScaler(feature_range=(0,1))

def main():
    f = sys.argv[1]
    n = sys.argv[2]
    columns = ["fav_novel_cnt","kaiwaritu","review_cnt","length","time","userid"]
    culc_columns = ["general_all_no","general_firstup","general_lastup"]

    df1 = pd.read_csv(f)
    df2 = df1[columns]
    df1 = df1[culc_columns]
    df2.userid = df2.userid.apply(lambda x:str(x))
    df2.length = df2.length.apply(lambda x: x/1000)
    #df2.fav_novel_cnt = df2.fav_novel_cnt.apply(lambda x: x/1000)
    #df2.fav_novel_cnt = pd.DataFrame(scale(df2.fav_novel_cnt.values))
    #df2.fav_novel_cnt = pd.DataFrame(mms.fit_transform((df2.fav_novel_cnt).values.reshape(-1,1)))
    df2.review_cnt = pd.DataFrame(scale(df2.review_cnt.values))
    df2.length = pd.DataFrame(scale(df2.length.values))
    df2.time = pd.DataFrame(scale(df2.time.values))

    # 任意に変更 ---
    download_time = "2018-11-09 00:00:00"
    download_time = datetime.datetime.strptime(download_time, "%Y-%m-%d %H:%M:%S")
    #df2.fav_novel_cnt = df2.fav_novel_cnt / (download_time - (df1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")))).apply(lambda x:x.total_seconds()).apply(lambda x: x/86400)
    df2.fav_novel_cnt = df2.fav_novel_cnt / (df1.general_lastup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) - df1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))).apply(lambda x:x.total_seconds()).apply(lambda x:86400 if x<86400 else x).apply(lambda x: x/86400)
    # ↑どうするか ---

    #df2 = pd.get_dummies(df2,columns=["userid"])

    # general_lastupの値を初投稿日から最後の投稿日の日数に ---
    df1.general_lastup = df1.general_lastup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")) - df1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    df1.general_lastup = df1.general_lastup.apply(lambda x:x.total_seconds()).apply(lambda x:86400 if x<86400 else x).apply(lambda x: x/86400)
    # general_firstupの値をunix_timeに変更して週単位にするか投稿されてからの日数にするか(下2行のどちらか、それによってrenameも選ぶ) ---
    #df1.general_firstup = df1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").timestamp()).apply(lambda x: x/604800)
    df1.general_firstup = (download_time - (df1.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S")))).apply(lambda x:x.total_seconds()).apply(lambda x: x/86400)
    df1 = df1.rename(columns={"general_firstup":"time_info","general_lastup":"dayup_ave"})
    df1.dayup_ave = df1.general_all_no / df1.dayup_ave # 値を1日毎の投稿頻度に

    #df1.time_info = pd.DataFrame(scale(df1.time_info.values))
    #df1.dayup_ave = pd.DataFrame(scale(df1.dayup_ave.values))
    #df1.general_all_no = pd.DataFrame(scale(df1.general_all_no.values))

    df1 = pd.concat([df2, df1], axis=1)

    df1 = pd.get_dummies(df1,columns=["userid"])

    #df1.to_csv("{0}.csv".format(n), index= False)
    df1 = sparse.csr_matrix(df1.to_sparse(), dtype=np.float32)
    save = pt(df1)
    save.save_pkl(n)



if __name__ == "__main__":
    main()