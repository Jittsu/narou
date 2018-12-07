# -*- coding: utf-8 -*-

import pandas as pd
import sys
import csv

def main():
    #l = []
    f1 = sys.argv[1]
    f2 = sys.argv[2]
    n = sys.argv[3]

    #l.append(pd.read_csv(f1, header=None))
    #l.append(pd.read_csv(f2, header=None))
    #df = pd.concat(l)

    df1 = pd.read_csv(f1)
    df2 = pd.read_csv(f2, header=None)

    df = pd.concat([df1, df2], axis=1)

    df.to_csv("{0}.csv".format(n), index=None, header=None)

if __name__ == "__main__":
    main()