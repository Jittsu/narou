# -*- coding: utf-8 -*-

"""
insert JSON data from *.json using bulk.
they are consisted of meta data of narou and
they have many comma separated JSON format data.
"""

"""
this is a code of inserting from "NAROU DATA" to elasticsearch
"""

import os
import glob
import sys
import json
from elasticsearch import Elasticsearch, helpers
es = Elasticsearch(timeout=180, max_retries=10, retry_on_timeout=True)

def main():
    dir = sys.argv[1]
    bulk_list = []
    path = dir + "*.json"

    for f1 in sorted(glob.glob(path)):
        print(f1)
        f2 = open(f1, "r")
        line = f2.readline()
        line = line.replace("{'",'{"').replace("'}",'"}').replace("': '",'": "').replace("', '",'", "').replace(", '",', "').replace("': ",'": ').replace(", \"\'",", \'\'")
        #line = line.replace('"s', "’s")
        data = json.loads(line)

        for j in data:
            #print(data1)

            try:

                #data3 = json.loads(data1)
                #data2 = json.dumps(data1[1:-1])
                #data3 = json.loads(data2)
                # index => _index, doc_type => _type, body => _source ---
                bulk_list.append({"_index":"narou_index","_type":"narou_type","_source":j}) # bulkに渡すリストへの追加 ---
            except:
                print('UNEXPECTED ERROR CAUSED')
                print(j)
                raise

        # 1000件たまったらbulk insert ---
        if len(bulk_list) > 1000:
            helpers.bulk(es, bulk_list)
            bulk_list = [] # 初期化 ---

        f2.close()

    # bulkに渡すリストが1000件に満たないままfor文終了時に残りをbulk insert ---
    if len(bulk_list) > 0:
        helpers.bulk(es, bulk_list)
        bulk_list = []

    print("ALL END")
    

if __name__ == "__main__":
    main()