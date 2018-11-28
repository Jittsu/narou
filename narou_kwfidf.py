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
from tfidf_to_pkl import tfidf_transformer as tt
from tfidf_to_pkl import pickle_transformer as pt


# 形態素解析 story => ['文書1の分かち書き(空白区切り)','文書2',...,'文書n']
def main(f): 
    f = csv.reader(open(f, "r"))
    header = next(f) # header削除 ---
    genre_bok = [] # bok: bag of keywords

    # 1作品ごとにkeywordをリストへ
    for line in f:
        keywords = line[23]
        genre_bok.append(keywords)
    return genre_bok

# tfidf値の計算 ---
def tfidf(corpus): # 引数の形は['文書1の分かち書き(空白区切り)','文書2',...,'文書n'] ---
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix.toarray())
    
    for k,v in sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1]):
        print(k, v)


if __name__ == "__main__":
    fin = sys.argv[1]
    #out = sys.argv[2]
    bok = main(fin)
    print(bok)
    #tfidf = tt("word")
    #model, matrix = tfidf.tfidf_culc(bow)
    #print(matrix.toarray())
    #save = pt(model)
    #save.save_pkl(out)