import sys  ,os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'indexing'))
import documents_indexing as documentsIndex
import tf_idf as tfidfClass
import pandas as pd
import  numpy  as np
from IPython.display import display
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'parsers'))
import dataset_reader as dr
import query_reader as qr
import query_result_reader as qrr
import pickle
import pandas as pd
import gensim
import query_reader as qr
from gensim.parsing.preprocessing import preprocess_documents
import dataset_testing as dt
from gensim import corpora



documents = None
bow_corpus = None
dictionary = None 
lsi = None
index = None
tfidf = None
def test():
    precisionList = []
    recallList = []
    MPR = []
    return dt.testQueries(dictionary,tfidf,lsi,index)

def initialize():
    global dictionary
    global bow_corpus
    global documents
    global lsi
    global index
    global tfidf
    documents = dr.read_all()
    filesContentsAfterTokenize = []
    for document in documents:    
        filesContentsAfterTokenize.append(document.abstract+document.author+document.title)
    processed_corpus = preprocess_documents(filesContentsAfterTokenize)
    dictionary = gensim.corpora.Dictionary(processed_corpus)
    bow_corpus = [dictionary.doc2bow(text) for text in processed_corpus]
    tfidf = gensim.models.TfidfModel(bow_corpus, smartirs='npu')
    corpus_tfidf = tfidf[bow_corpus]
    lsi = gensim.models.LsiModel(corpus_tfidf, num_topics=450)
    index = gensim.similarities.MatrixSimilarity(lsi[corpus_tfidf])
    return dictionary,tfidf,lsi,index,documents


def topicDetect ():
    NUM_TOPICS = 5
    ldamodel = gensim.models.ldamodel.LdaModel(bow_corpus, num_topics = NUM_TOPICS, id2word=dictionary, passes=15)
    topics = ldamodel.print_topics(num_words=4)
    return topics
