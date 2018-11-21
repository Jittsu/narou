# -*- coding: utf-8 -*-

"""
test of seaborn
"""

import seaborn as sns
import pandas as pd
import numpy as np
#import sys
import matplotlib.pyplot as plt

def main():
    #f = sys.argv[1]
    #df = pd.read_csv(f)
    iris = sns.load_dataset("iris")
    sns.pairplot(iris)
    plt.show()
    

if __name__ == "__main__":
    main()