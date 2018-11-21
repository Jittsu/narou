import os
import glob
import sys
import json
import pandas as pd
from elasticsearch import Elasticsearch, helpers
es = Elasticsearch(timeout=180, max_retries=10, retry_on_timeout=True)


dir = sys.argv[1]
bulk_list = []
path = dir + "*.json"
cnt = 0

for f1 in sorted(glob.glob(path)):
        print(f1)
        f2 = open(f1, "r")
        line = f2.readline()
        line = line.replace("{'",'{"').replace("'}",'"}').replace("': '",'": "').replace("', '",'", "').replace(", '",', "').replace("': ",'": ').replace(", \"\'",", \'\'")
        data = json.loads(line)

        for j in data:
               cnt += 1 
print(cnt)