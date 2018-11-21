# -*- coding: utf-8 -*-

"""
using csv file of NAROU from Elasticsearch
this is a code of culculating TF-IDF value of story
"""

import os
import sys
#import glob
import MeCab
import csv
import pickle
#import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer

# 形態素解析 story => ['文書1の分かち書き(空白区切り)','文書2',...,'文書n']
def wakati():
    mecab = MeCab.Tagger("wakati")
    mecab.parse('') # エラー避け ---   
    f = sys.argv[1]
    f = csv.reader(open(f, "r"))
    genre_bow = []

    # 1作品ごとにstoryをBoWに
    for line in f:
        story = ""
        #print("---")
        #print(line[31])
        words = mecab.parse(line[31])
        #print(words)
        words = words.split("\n") # 分かち書きごとに分割 ---

        # 分かち書きした単語をリストに投入 ---
        for word in words:
            #print(word)
            w1 = re.split(r"[\t,]", word)
            #print(w1)

            if (w1[0] == "EOS") | (w1[0] == ""):
                continue
            else:

                if (w1[1] == "形容詞") | (w1[1] == "接続詞") | (w1[1] == "動詞") | (w1[1] == "名詞") | (w1[1] == "副詞"):

                    if w1[7] == "*":
                        #print(w1[7])
                        #print(w1)
                        #w1[7] = w1[0]
                        #print(w1[7])
                        continue # 数とかしかない ---
                    #print(w1[7])
                    #story.append(w1[7])
                    story = story + w1[7] + " " # 空白区切りのBoWを作る ---
        #print(story)
        genre_bow.append(story)
        #print(genre_bow)
    return genre_bow

# tfidf値の計算 ---
def tfidf(corpus): # 引数の形は['文書1の分かち書き(空白区切り)','文書2',...,'文書n'] ---
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix)


if __name__ == "__main__":
    bow = wakati()
    tfidf(bow)