# -*- coding: utf-8 -*-

"""
using csv file of NAROU from Elasticsearch
this is a code of culculating TF-IDF value of story
argv[1]: NAROU csv data, argv[2]: output name (ex: argv[2].pkl)
"""

import os
import sys
import MeCab
import csv
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from tfidf_to_pkl import tfidf_transformer as tt
from tfidf_to_pkl import pickle_transformer as pt


# 形態素解析 story => ['文書1の分かち書き(空白区切り)','文書2',...,'文書n'] ---
def wakati(f):
    mecab = MeCab.Tagger("wakati")
    mecab.parse('') # エラー避け ---   
    f = csv.reader(open(f, "r"))
    header = next(f) # header削除 ---
    genre_bow = []

    # 1作品ごとにstoryをBoWに ---
    for line in f:
        story = ""
        words = mecab.parse(line[31])
        words = words.split("\n") # 分かち書きごとに分割 ---

        # 分かち書きした単語をリストに投入 ---
        for word in words:
            w1 = re.split(r"[\t,]", word)

            if (w1[0] == "EOS") | (w1[0] == ""):
                continue
            else:

                if (w1[1] == "形容詞") | (w1[1] == "接続詞") | (w1[1] == "動詞") | (w1[1] == "名詞") | (w1[1] == "副詞"):

                    if w1[7] == "*":
                        continue # 数とかしかない ---
                    story = story + w1[7] + " " # 空白区切りのBoWを作る ---
        genre_bow.append(story)
    return genre_bow

# tfidf値の計算 ---
def tfidf(corpus): # 引数の形は['文書1の分かち書き(空白区切り)','文書2',...,'文書n'] ---
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(tfidf_matrix.toarray())
    
    for k,v in sorted(vectorizer.vocabulary_.items(), key=lambda x:x[1]):
        print(k, v)


if __name__ == "__main__":
    fin = sys.argv[1]
    out = sys.argv[2]
    bow = wakati(fin)
    #print(bow)
    #tfidf(bow)
    tfidf = tt("word")
    model, matrix = tfidf.tfidf_culc(bow)
    #print(matrix.toarray())
    save = pt(model)
    save.save_pkl(out)