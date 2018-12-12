# -*- coding: utf-8 -*-

"""
using csv file of NAROU from Elasticsearch
this is a code of culculating TF-IDF value of keyword and one word is one keyword so it is not using MeCab
argv[1]: NAROU csv data, argv[2]: output name (ex: argv[2].pkl)
"""

import os
import sys
import csv
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from tfidfTransformer import tfidf_transformer as tt
from tfidfTransformer import pickle_transformer as pt
from tfidfTransformer import csv_transformer as ct


# メニュー ---
def main():
    tfidf = tt("word")
    while(1):
        print("select mode")
        print("you can get pickle output if you put \"pickle\"")
        print("you can get csv output if you put \"csv\"")
        print("you can finish if you put \"end\"")

        mode = input(">> ")

        if mode == "pickle":
            print("select csv file what you want to transform to pickle")
            fin = input(">> ")
            print("put a name of output file")
            out = input(">> ")
            bow = wakati(fin)
            model, matrix = tfidf.tfidf_culc(bow)
            save = pt(matrix)
            save.save_pkl(out)

        elif mode == "csv":
            print("select csv file what you want to transform to csv")
            fin = input(">> ")
            print("put a name of output file")
            out = input(">> ")
            bow = wakati(fin)
            model, matrix = tfidf.tfidf_culc(bow)
            save = ct(matrix)
            save.save_csv(out)

        elif mode == "end":
            print("end")
            break

        else:
            continue


# 形態素解析 keyword => ['文書1の分かち書き(空白区切り)','文書2',...,'文書n'] ---
def wakati(f):
    f = csv.reader(open(f, "r"))
    header = next(f) # header削除 ---
    keywords = []

    # 1作品ごとにkeywordをBoWに ---
    for line in f:
        key = ""
        words = line[23]
        words = words.split(" ") # キーワードに分割 ---

        # キーワードをリストに投入 ---
        for word in words:

            if (word == "R15") | (word == "残酷な描写あり"):
                continue
            else:
                key = key + word + " " # 空白区切りのBoWを作る ---
        keywords.append(key)
    return keywords


if __name__ == "__main__":
    main()