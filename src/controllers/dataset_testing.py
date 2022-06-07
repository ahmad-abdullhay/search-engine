from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
import sys,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'indexing'))

import tf_idf as tfidfClass
import documents_indexing as documentsIndex
import pickle
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'parsers'))

import query_reader as qr
import query_result_reader as qrr
import query_model
import query as q
import gensim

from gensim.parsing.preprocessing import preprocess_documents
def getQueryResult (queryModel,queryResultList):
    for queryResult in queryResultList:
        if (queryResult.id == queryModel.id):
            return queryResult

def matchQueryWithQueryResult (queryResult,related_docs_indices):
    resultList = []
    for index in related_docs_indices:
       resultList.append(queryResult.isMatch(index)) 
    return resultList

def rr (trueList):
    for index,r in enumerate(trueList): 
        if (r):
            return 1/(index+1)
    return 0
def avp (trueList):
    total = 0
    trueCount = 0
    for index,r in enumerate(trueList): 
        if (r):
            trueCount+=1
            total+= trueCount/(index+1)
            
    return total/10

def testQueries (dictionary,tfidf,lsi,index):
    queryResultList = qrr.readAllQueriesResult()
    queryList = qr.readAllQueries()
    evList = []
    
    for queryModel in queryList:
        query = queryModel.query
        new_doc = gensim.parsing.preprocessing.preprocess_string(query+queryModel.author+queryModel.title)
        new_vec = dictionary.doc2bow(new_doc)
        vec_bow_tfidf = tfidf[new_vec]
        vec_lsi = lsi[vec_bow_tfidf]
        sims = index[vec_lsi]
        queryResult = getQueryResult(queryModel,queryResultList)
        if (queryResult is not None):
            x = []
            for s in sorted(enumerate(sims), key=lambda item: -item[1])[:10]:
                x.append(s[0])
            trueList = matchQueryWithQueryResult(queryResult,x)
            sumOfTrues = sum(trueList)
            ev = {'queryModel' :queryModel,
            'sumOfTrues' :sumOfTrues,
            'queryResult' :queryResult,
            'rr' : rr(trueList),
             'avp':avp(trueList),
            '@k' :10,
            }
            evList.append(ev)
    return evList


