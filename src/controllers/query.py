from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'indexing'))
from textblob import TextBlob
import tf_idf as tfidfClass
import documents_indexing as documentsIndex
import pickle
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'parsers'))
import requests
import json
from fake_useragent import UserAgent
import query_reader as qr
import query_result_reader as qrr
import query_model
import main as m
import gensim
dictionary = None
tfidf = None
lsi = None 
index = None

def initTfidf ():
    global dictionary
    global tfidf
    global lsi
    global index
    dictionary,tfidf,lsi,index,documents = m.initialize()
    return documents



    
def searchByString (queryString):

    new_doc = gensim.parsing.preprocessing.preprocess_string(queryString)
    new_vec = dictionary.doc2bow(new_doc)
    vec_bow_tfidf = tfidf[new_vec]
    vec_lsi = lsi[vec_bow_tfidf]
    sims = index[vec_lsi]
    x = []
    for s in sorted(enumerate(sims), key=lambda item: -item[1])[:10]:
        x.append(s[0])
    return x


def queryCorrection (queryString):
    sentence = TextBlob(queryString)
    result = sentence.correct()
    return result


def querySuggestion (queryString):
    url = "http://suggestqueries.google.com/complete/search?output=firefox&q=" + queryString
    ua = UserAgent()
    headers = {"user-agent": ua.chrome}
    response = requests.get(url, headers=headers, verify=False)
    suggestions = json.loads(response.text)
    results = []
    for word in suggestions[1]:
        results.append(word)
    return results
