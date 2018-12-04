# -*- coding: utf-8 -*-

"""
this code was written using the code from https://qiita.com/arata-honda/items/6409e387027c31365741 as a reference
"""


from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import csv


class tfidf_transformer:

    def __init__(self, analyze_method):
        self.vectorizer = TfidfVectorizer(analyzer=analyze_method, use_idf=True, norm='l2', smooth_idf=True)

    def tfidf_culc(self, corpus): # 引数の形は['文書1の分かち書き(空白区切り)','文書2',...,'文書n'] ---
        tfidf_model = self.vectorizer.fit(corpus)
        tfidf_matrix = self.vectorizer.transform(corpus)
        return tfidf_model, tfidf_matrix


class pickle_transformer:

    def __init__(self, model):
        self.model = model

    def save_pkl(self, name):
        try:
            with open("{0}.pkl".format(name), "wb") as f:
                pickle.dump(self.model, f)
            return print("ok")
        except:
            return print("error")

class csv_transformer:

    def __init__(self, matrix):
        self.matrix = matrix.toarray()

    def save_csv(self, name):
        try:
            with open("{0}.csv".format(name), "w") as f:
                writer = csv.writer(f, lineterminator='\n')
                writer.writerows(self.matrix)
            return print("ok")
        except:
            return print("error")
