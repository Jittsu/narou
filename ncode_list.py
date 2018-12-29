# -*- coding: utf-8 -*-

import pandas as pd
import sys

def main():
    fin = sys.argv[1]
    n = sys.argv[2]

    df = pd.read_csv(fin)
    df = df[["ncode", "fav_novel_cnt"]]
    #print(df)

    df.to_csv("{0}.csv".format(n), index=False)

if __name__ == "__main__":
    main()
