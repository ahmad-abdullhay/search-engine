from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import my_helper_functions as MyHelperFunctions
import re
def getDocumentIndexes (contents):
    sentenceTokens = sent_tokenize(contents)
    wordTokens = word_tokenize(contents)

    wordTokens = [word.lower() for word in wordTokens]
    wordTokens = [word for word in wordTokens if not word in stopwords.words("english")]

    # this function turn every date token to 3 sperete tokens with specified format
    # (date and time, time only, date only)

    wordTokens = MyHelperFunctions.myDateParser(wordTokens)
    # remove every token with no latters or numbers        
    wordTokens = [word for word in wordTokens if re.match('.*[a-zA-Z0-9].*', word)]

    ps = PorterStemmer()
    wordTokensStemmed = [ps.stem(word) for word in wordTokens]

    tagged = nltk.pos_tag(wordTokens)
    stemmedTagged = nltk.pos_tag(wordTokensStemmed)

    lemmatizer = WordNetLemmatizer()
    #wordTokensLemm = [lemmatizer.lemmatize(word[0],pos=MyHelperFunctions.get_wordnet_pos(word[1])) for word in tagged]
    stemmedWordTokensLemm = [lemmatizer.lemmatize(word[0],pos=MyHelperFunctions.get_wordnet_pos(word[1])) for word in stemmedTagged]
   
    return stemmedWordTokensLemm



