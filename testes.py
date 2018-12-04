import os
import glob
import sys
import json
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from elasticsearch import Elasticsearch, helpers
es = Elasticsearch(timeout=180, max_retries=10, retry_on_timeout=True)

print("select mode")
 
while(1):
    mode = input(">> ")

    if mode == "csv":
        print("csv output")

    elif mode == "pickle":
        print("pickle output")

    elif mode == "end":
        print("end")
        break

    else:
        continue