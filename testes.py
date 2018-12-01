import os
import glob
import sys
import json
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from elasticsearch import Elasticsearch, helpers
es = Elasticsearch(timeout=180, max_retries=10, retry_on_timeout=True)

f = sys.argv[1]

df = pd.read_csv(f)
df = df["length"]

sns.distplot(df)
plt.xscale("log")
plt.yscale("log")
plt.show()