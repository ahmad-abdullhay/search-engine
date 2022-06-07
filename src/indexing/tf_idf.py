from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
from IPython.display import display


def tfidfFunction (files):
    tfidf = TfidfVectorizer(ngram_range=(1,1))
    result = tfidf.fit_transform(files)
    return result, tfidf

def displayResultAsDataFrames(result):
    df = pd.DataFrame(result)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print('tfidf table')
        df.to_csv('newdf.csv')

def displayQueryAsDataFrames(result):
    dense = result.todense()
    denselist = dense.tolist()
    df = pd.DataFrame(denselist)
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        df.to_csv('queryDF.csv')