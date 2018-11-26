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

def main():
    sns.set()
    f = sys.argv[1]
    df = pd.read_csv(f)
    df = df[["fav_novel_cnt","length","all_point","general_all_no","review_cnt","kaiwaritu"]]
    #df.length = df.length.apply(lambda x:int(x.replace(",","")))
    #df.fav_novel_cnt = df.fav_novel_cnt.apply(lambda x:int(x.replace(",","")))
    #df.all_point = df.all_point.apply(lambda x:int(x.replace(",","")))
    #df = df[df.fav_novel_cnt > 100]
    #print(df.head())
    #print(df.tail())
    #print(df)
    sns.pairplot(df)
    #graph = sns.pairplot(df)
    #sns.jointplot("sasie_cnt","kaiwaritu", data=df)
    #plt.xscale("log")
    #plt.yscale("log")
    #graph.set(xscale="log", yscale="log")
    plt.show()
    

if __name__ == "__main__":
    main()