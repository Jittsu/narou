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
    df = df[["fav_novel_cnt","kaiwaritu","review_cnt","length","time","general_all_no","time_info","dayup_ave"]]
    df.review_cnt = df.review_cnt.apply(lambda x: np.log(x+1))
    df.length = df.length.apply(lambda x: np.log(x+1))
    df.time = df.time.apply(lambda x: np.log(x+1))
    df.general_all_no = df.general_all_no.apply(lambda x: np.log(x+1))
    #df.time_info = df.time_info.apply(lambda x: np.log(x+1))
    df.dayup_ave = df.dayup_ave.apply(lambda x: np.log(x+1))
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
    sns.pairplot(df)
    #graph = sns.pairplot(df)
    #sns.jointplot("fav_novel_cnt", "general_firstup", data=df)
    #plt.xscale("log")
    #plt.yscale("log")
    #graph.set(xscale="log")
    plt.savefig("seaborn.png")
    #plt.show()
    

if __name__ == "__main__":
    main()
