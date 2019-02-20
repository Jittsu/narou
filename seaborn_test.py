# -*- coding: utf-8 -*-

"""
test of seaborn
"""

import seaborn as sns
import pandas as pd
import numpy as np
#import sys
import matplotlib.pyplot as plt
import sys
import datetime

def main():
    sns.set()
    f = sys.argv[1]
    df = pd.read_csv(f)
    df = df[["fav_novel_cnt","global_point", "all_point"]]
    #df = df.todense()
    #df = pd.DataFrame(df)
    #print(df)
    df_corr = df.corr()
    #plt.rcParams['font.family'] = 'IPAPGothic'
    #df.review_cnt = df.review_cnt.apply(lambda x: np.log(x+1))
    #df.length = df.length.apply(lambda x: np.log(x+1))
    #df.time = df.time.apply(lambda x: np.log(x+1))
    #df.general_all_no = df.general_all_no.apply(lambda x: np.log(x+1))
    #df.time_info = df.time_info.apply(lambda x: np.log(x+1))
    #df.dayup_ave = df.dayup_ave.apply(lambda x: np.log(x+1))
    #download_time = "2018-11-09 00:00:00"
    #download_time = datetime.datetime.strptime(download_time, "%Y-%m-%d %H:%M:%S")
    #df.general_firstup = download_time - df.general_firstup.apply(lambda x:datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S"))
    #df.general_firstup = df.general_firstup.apply(lambda x:(x.total_seconds())/86400)
    #df.length = df.length.apply(lambda x:int(x.replace(",","")))
    #df.fav_novel_cnt = df.fav_novel_cnt.apply(lambda x:int(x.replace(",","")))
    #df.all_point = df.all_point.apply(lambda x:int(x.replace(",","")))
    #df = df[df.fav_novel_cnt > 100]
    #print(df.head())
    #print(df.tail())
    #print(df)
    #sns.distplot(df["fav_novel_cnt"], kde=False)
    #sns.pairplot(df)
    #graph = sns.pairplot(df)
    #sns.regplot("fav_novel_cnt", "global_point", data=df, fit_reg=False)
    #sns.relplot("fav_novel_cnt", "global_point", data=df)
    sns.heatmap(df_corr, square=True, annot=True)
    #plt.xscale("log")
    #plt.yscale("log")
    #graph.set(xscale="log")
    #plt.savefig("seaborn.png")
    print(df_corr)
    #plt.title("相関係数:%s" % df_corr)
    plt.show()
    

if __name__ == "__main__":
    main()
