# -*- coding: utf-8 -*-

"""
test of reading csv using pandas
"""

import pandas as pd
import sys

def main():
    f = sys.argv[1]
    columns = ["fav_novel_cnt", "all_point", "global_point"]

    df = pd.read_csv(f)
    df = df[columns]
    df.to_csv("/mnt/hdd1/data/narou/test.csv")

    #print(df)


if __name__ == "__main__":
    main()