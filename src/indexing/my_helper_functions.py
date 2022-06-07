from nltk.corpus import wordnet
import dateutil.parser as dateparser
import datetime

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        # As default pos in lemmatization is Noun
        return wordnet.NOUN


# turn every date to 3 sperete tokens with specified format
# (date and time, time only, date only)
# example
# date = '1/7/1999'
# time = '8:30 am'
# dateAndTime = '8:30 am 1/7/1999'
# print (MyHelperFunctions.myDateParser([date]))
# print (MyHelperFunctions.myDateParser([time]))
# print (MyHelperFunctions.myDateParser([dateAndTime]))
def myDateParser (tokens):
    for i,word in enumerate(tokens):
        if not(word.isalpha() or word.isnumeric()):
            try:
                tokens[i] = dateparser.parse(word,fuzzy=False)
            except:
                ignore =''

    for i,word in enumerate(tokens):
        if isinstance(word, datetime.datetime):
            tokens[i] = word.strftime('%m/%d/%Y')
            tokens.insert(i,word.strftime('%H:%M:%S'),)
            tokens.insert(i,word.strftime('%m/%d/%Y, %H:%M:%S'))
    return tokens
