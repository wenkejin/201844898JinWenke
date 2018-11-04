import math
import os 
from nltk.curpus import stopword
from textblob import TextBlob
from textblob import Word

def knn(path):
    trainSet = {}
    testSet = {}
    trainVocabulary = []
    testVocabulary = []
    files = os.listdir(path)
    for file in files:
        documents = os.listdir(path + "/" + file)
        trainSetLength = int(0.8 * len(document))
        testSetLength = int(0.2 * len(document))
        for i in range(trainSetLength):
            trainVocabulary = []
            documentContent = path + "/" + file + "/" + documents[i + trainSetLength]
            with open(documentContent,'r',errors='ignort') as f:
                data=f.readlines()
                for i in data:
                    temp = i.split(":")[1]
                    trainVocabulary.append(float(temp))  
        for j in range(testSetLength):
            trainVocabulary = []
            documentContent = path + "/" + file + "/" + documents[i + testSetLength]
            with open(documentContent,'r',errors='ignort') as f:
                data=f.readlines()
                for j in data:
                    temp = j.split(":")[1]
                    testVocabulary.append(float(temp)) 
    for k in range(trainSetLength):
        molecular += trainSet[k] * testSet[k]
        denominator += trainSet[k]*trainSet[k] + testSet[k]*testSet[k]
    if denominator > 0:
        return molecular /(pow(denominator, 0.5))
             
if __name__ == '__main__':
    path = 'C:/Users/wk/Desktop/20news-18828'
    knn(path)