#import nltk
#from nltk.corpus import PlaintextCorpusReader
from collections import Counter
import numpy as np

dirpath = "C:\Users\Daniela\Documents\221Essay"

'''
def naiveClassifier():
    #folder = nltk.data.find(dirpath)
    #print(folder)
    text = PlaintextCorpusReader(dirpath,'.*\.txt')
    print (text.sents())
    numSentences = len(text.sents())
    numParas = len(text.paras())
    numWords = len([word for sent in text.sents() for word in sent])
    
    uniqueWords = set([word for sent in text.sents() for word in sent])
    
    numUniqueWords = len(uniqueWords)
    
    sumWordLength = sum([len(word) for sent in text.sents() for word in sent])
    
    #avgWordLength = sumWordLength/numWords
    
    sentLengths = [len(sent) for sent in text.sents()]
    avgSentenceLength = sum(sentLength)/len(sentLength)
    varSentLen = np.var(sentLengths)
    
    weights = np.array([.1, .2, .1, .2, .2, .2])
    features = np.array([numWords, numParas, numSentences, avgSentenceLength, varSentLen, numUniqueWords])
    
    score =  np.dot(features, weights)
'''


def naiveClassifier(text):
    text = open(text, "r")    
    wordCount = Counter(text.read().split())
    words = 0
    sentence = 0
    sentLength = np.array([])
    distinctWords = set([item[0] for item in wordCount.items()])
    
    i = 0
    for item in wordCount.items():
        #print item
        words += item[1]
        i+=1
        if item[0].endswith("."):
            sentence+=1
            #print sentence
            sentLength = np.append(sentLength, i)
            i=0
    #print sentLength
    variance = np.var(sentLength)
    avgSentLength = sum(sentLength)/len(sentLength)
    
    features = np.array([words, sentence, avgSentLength, variance, len(distinctWords)])
    
    weights = np.array([.2, .2, .2, .2, .2])
    
    score = np.dot(features, weights)
    if score > 800:
        print 5
        return 5
    elif score > 600:
        print 4
        return 4
    elif score > 400:
        print 3
        return 3
    elif score > 200:
        print 2
        return 2
    else: 
        print 1
        return 1
    
    
    
  
text = "essay.txt"
naiveClassifier(text)
    
 