# -*- coding: utf-8 -*-

import pickle
import sys
import pandas as pd
import numpy as np
from scipy import sparse
from tfidfTransformer import pickle_transformer as pt

def main():
    f1 = sys.argv[1] # from csv_preprocess.py ---
    f2 = sys.argv[2] # from narou_kwfidf.py ---
    n = sys.argv[3] # name ---

    f1 = pd.read_pickle(f1) # str => scipy.sparse.csv.csr_matrix ---
    f2 = pd.read_pickle(f2)

    f1 = f1.todense() # scipy.sparse.csv.csr_matrix => numpy.matrixlib.defmatrix.matrix ---
    f2 = f2.todense()

    out = np.concatenate([f1, f2], axis=1)
    out = sparse.csr_matrix(out, dtype=np.float32) # numpy.matrixlib.defmatrix.matrix => scipy.sparse.csv.csr_matrix ---

    save = pt(out)
    save.save_pkl(n)


if __name__ == "__main__":
    main()