import os
import glob
import sys
import json
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from elasticsearch import Elasticsearch, helpers
from sklearn.preprocessing import scale

es = Elasticsearch(timeout=180, max_retries=10, retry_on_timeout=True)

df = pd.DataFrame(data=[[1,1,1],[1,0.5,1],[1,0,1]])
df1 = df.iloc[:,1]
df2 = df1.values
df3 = scale(df2)
df4 = pd.DataFrame(df3)
df[1] = df4
print(df)