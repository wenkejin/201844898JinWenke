import math
import os  
from nltk.curpus import stopword
from textblob import TextBlob
from textblob import Word

def vsm(path):
    vocabulary = {}
    IF = []
    IDF = []
    weight = []
    files = os.listdir(path)
    for file in files:
        documents = os.listdir(path + '/' + file)
        for document in documents:
            documentContent = open(path + '/' + flie + '/' + document, 'r', errors = 'ignore')
            data = documentContent.readlines()
            data = str(data).lower()
            data = TextBlob(str(data).replace("\\n", "").replace("\\t", "").replace("\\", "").replace("'", ''))
            data = data.words
            data = [word for word in data if(word not in stopword.words('english'))]
            for word in data:
                for i in data:
                    count = 0
                    if word = data.get(i):
                        count++
                IF[word] = count / len(data)
            vocabulary.append(data)
    files = os.listdir(path)
    for file in files:
        documents = os.listdir(path + '/' + file)
        count = 0
        for document in documents:
            documentContent = open(path + '/' + flie + '/' + document, 'r', errors = 'ignore')
            data = documentContent.readlines()
            for word in vocabulary:
                if word == data:
                    count++
            IDF[word] = log(len(vocabulary) / (count + 1))
    for word in vocabulary:
        weight[word] = IF[word] * IDF[word]
    for file in files:
        documents = os.listdir(path + '/' + file)
        for document in documents:
            documentContent = open(path + '/' + flie + '/' + document, 'r', errors = 'ignore')
            data = documentContent.readlines()
            for word in vocabulary:
                if data == word:
                    document = vocabulary{word : weight[word]}
                    			
if __name__ == 'main':
    path = 'C:/Users/wk/Desktop/20news-18828'
    vsm(path)
