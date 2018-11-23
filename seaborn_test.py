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
    df = df[["length","fav_novel_cnt","all_point","general_all_no","review_cnt","sasie_cnt","kaiwaritu"]]
    print(df)
    sns.pairplot(df)
    #sns.jointplot("sasie_cnt","kaiwaritu", data=df)
    plt.show()
    

if __name__ == "__main__":
    main()