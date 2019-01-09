# -*- coding: utf-8 -*-

import requests
import json
import datetime
import os
import time
import random
import pandas as pd

if __name__ == "__main__":
    crawl_start = datetime.date.today()
    #dirpath = "/mnt/hdd1/data/raw/{0}".format(crawl_start)
    dirpath1 = "/mnt/hdd1/data/narou/2019/narou_{0}/".format(crawl_start) # ディレクトリ指定 2018-12-19 ---
    os.mkdir(dirpath1)
    dirpath2 = "/mnt/hdd1/data/narou/2019/narou_{0}/raw/".format(crawl_start)
    os.mkdir(dirpath2)

    #done_novel = os.listdir("/mnt/hdd1/data/raw")
    done_novel = os.listdir("/mnt/hdd1/data/narou/2019/narou_{0}/raw".format(crawl_start)) # ディレクトリ指定 2018-12-19 ---
    # ncodeの出力 ---
    for i in range(26*2, 26*7): # n****a~n****fc<-までにしたい ---
        if i < 26:
            alpha_id = chr(ord('a') + i)
        else:
            alpha_id = chr(ord('a') + ((i // 26) - 1)) + chr(ord('a') + (i % 26))
        for j in range(1000):
            ncode = ""
            for k in range(10):
                ncode += "n{0:04d}{1}-".format(j*10+k, alpha_id)
            api = "http://api.syosetu.com/novelapi/api/?&out=json&ncode={0}"
            ncode = ncode[:-1]
            url = api.format(ncode)

            f = ncode.split("-")[0] + "-" + ncode.split("-")[-1] + ".json"
            if f in done_novel:
                print("小説 {0} はクロール済みなのでスキップします。".format(f))
                continue
            sleep_time = random.choice([0.1, 0.2, 0.3])
            time.sleep(sleep_time)
            crawl_time = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            try:
                r = requests.get(url).json()
            except Exception as e:
                with open("errorlog.txt", "a")as efp:
                    errtxt = "{0},{1}:{2}\n".format(crawl_time,f,e)
                    efp.write(errtxt)
                print(e)
            if len(r) >= 2:
                print("小説 {0} のクローリングを行います。".format(f))
                novel = None
                #fname = "/mnt/hdd1/data/raw/{0}".format(f)
                fname = "/mnt/hdd1/data/narou/2019/narou_{0}/raw/{1}".format(crawl_start,f) # ディレクトリ指定 2018-12-19 ---
                with open(fname, "w") as File:
                    File.write(str(r[1:]))
            else:
                print("小説 {0} は存在しません。".format(f))
