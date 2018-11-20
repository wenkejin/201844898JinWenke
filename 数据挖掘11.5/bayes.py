import nltk
import operator
import re
from nltk.corpus import stopwords	
from numpy import *
from os import listdir, makedirs, mkdir, path

def dataProcess():
    ##print("enter dataProcess")

    fileList = listdir(sourcePath)
    for file in fileList:
        documentList = listdir(sourcePath + '/' + file)
        if path.exists(targetPath) == False:
            makedirs(targetPath)
        else:
            print("jwkError:%s exists" % targetPath)
        for document in documentList:
            fw = open(targetPath + '/' + file + '/' + document, 'w')
            dataList = open(sourcePath + '/' + file + '/' + document, errors = 'ignore').readlines()
            for line in dataList:
                stopwords = nltk.corpus.stopwords.words('english')
                splitter = re.compile('[^a-zA-Z]')
                porter = nltk.PorterStemmer()
                words = [porter.stem(word.lower()) for word in splitter.split(line) if len(word) > 0 and word.lower() not in stopwords]
                for word in words:
                    fw.write(word + '\n')
            fw.close()
            ##print("%s %s" % (file, document))
            
    print("end dataProcess")	 

def dictionaryConstruction():
    ##print("enter dictionaryConstruction")

    wordMap = {}
    dictionary ={}
    fileList = listdir(targetPath)
    for file in fileList:
        documentList = listdir(targetPath + '/' + file)
        for document in documentList:
            dataList = open(targetPath + '/' + file + '/' + document, errors = 'ignore').readlines()
            for line in  dataList:
                word = line.strip('\n')
                wordMap[word] = wordMap.get(word, 0.0) + 1.0
    for key, value in wordMap.items():
        if value > 4:
            dictionary[key] = value
    dictionary = sorted(dictionary.items())
    print('wordMap size : %d' % len(wordMap))
    print('dictionary size : %d' % len(dictionary))
    countLine = 0
    fw = open('F:/20news-18828_Dictionary/20news-18828_Dictionary.txt', 'w')
    for item in dictionary:
        fw.write("%s %.1f\n" % (item[0], item[1]))
        countLine += 1        
    print('dictionary size : %d' % countLine)
    fw.close()
    return dictionary
    
    ##print("end dictionaryConstruction")

def characteristicWordFilter():
    ##print("enter characteristicWordFilter")
    
    Dictionary = {}
    dictionary = dictionaryConstruction()
    for i in range(len(dictionary)):
        Dictionary[dictionary[i][0]] = dictionary[i][0]  
    fileList = listdir(targetPath)
    for file in fileList:
        documentList = listdir(targetPath + '/' + file)
        if path.exists(targetPath2 + '/' + file) == False:
            makedirs(targetPath2 + '/' + file)
        else:
            print("jwkError:%s exists" % targetPath2)
        for document in documentList:
            fw = open(targetPath2 + '/' + file + '/' + document, 'w')
            dataList = open(targetPath + '/' + file + '/' + document, errors = 'ignore').readlines()
            for line in dataList:
                word = line.strip('\n')
                
                if word in Dictionary.keys():
                    fw.write("%s\n" % word)
            fw.close()
     
    ##print("enter characteristicWordFilter")

def createTestSet(indexOfExperiment, classifyRight, trainSetPercent = 0.8):
    fw = open(classifyRight, 'w')
    fileList = listdir(targetPath2)
    for file in fileList:
        documentList = listdir(targetPath2 + '/' + file)
        testBeginIndex = indexOfExperiment * (len(documentList) * (1 - trainSetPercent)) 
        testEndIndex = (indexOfExperiment + 1) * (len(documentList) * (1 - trainSetPercent))
        for document in documentList:
            if (j > testBeginIndex) and (j < testEndIndex): 
                fw.write('%s %s\n' % (document,file)) 
                targetPath3 = 'F:/TestSet' + str(indexOfExperiment) + '/' + file 
            else:
                targetPath3 = 'F:/TrainSet' + str(indexOfExperiment) + '/' + file 
            if path.exists(targetPath3) == False:
                mkdir(targetPath3)           
            documentList = open(fileList).readlines()
            documentListWriter = open(targetPath3 + '/' + document, 'w')
            for line in documentList:
                documentListWriter.write('%s\n' % line.strip('\n'))
            documentListWriter.close()
    fw.close()
　　def test():
   　　 for i in range(10):
      　　  classifyRight = 'classifyRightCate' + str(i) + '.txt'
        　　createTestdocumentList(i, classifyRight)

def naiveBayesProcess(trainPath, testPath, classifyResultFileNew):
    fw = open(classifyResultFileNew,'w')   
    cateWordsNum = {}
    cateWordsProb = {}
    cateDir = listdir(strDir)
    for i in range(len(cateDir)):
        count = 0  
        fileList = strDir + '/' + cateDir[i]
        documentList = listdir(fileList)
        for j in range(len(documentList)):
            documentListFile = fileList + '/' + documentList[j]
            words = open(documentListFile).readlines()
            for line in words:
                count = count + 1
                word = line.strip('\n')                
                keyName = cateDir[i] + '_' + word
                cateWordsProb[keyName] = cateWordsProb.get(keyName,0)+1 
        cateWordsNum[cateDir[i]] = count
    trainTotalNum = sum(cateWordsNum.values()) 
    testDirFiles = listdir(testdir)
    for i in range(len(testDirFiles)):
        testfileList = testdir + '/' + testDirFiles[i]
        testdocumentList = listdir(testfileList)
        for j in range(len(testdocumentList)):
            testFilesWords = []
            fileList = testfileList + '/' + testdocumentList[j]
            lines = open(fileList).readlines()
            for line in lines:
                word = line.strip('\n')
                testFilesWords.append(word)
			maxP = 0.0
            trainDirFiles = listdir(traindir)
            for k in range(len(trainDirFiles)):
                if k == 0:
                    bestCate = trainDirFiles[k]
                else:
                    bestCate = trainDirFiles[k]
            fw.write('%s %s\n' % (testdocumentList[j], bestCate))
    fw.close()

def computeAccuracy(rightCate, resultCate, k):
    rightCateDict = {}
    resultCateDict = {}
    rightCount = 0.0
    for line in open(rightCate).readlines():
        (documentListFile,cate) = line.strip('\n').split(' ')
        rightCateDict[documentListFile] = cate      
    for line in open(resultCate).readlines():
        (documentListFile,cate) = line.strip('\n').split(' ')
        resultCateDict[documentListFile] = cate     
    for documentListFile in rightCateDict.keys():      
        if (rightCateDict[documentListFile] == resultCateDict[documentListFile]):
            rightCount += 1.0
    accuracy = rightCount/len(rightCateDict)
    return accuracy

if __name__ == "__main__":
    ##print("enter main")
    
    sourcePath = 'F:/20news-18828'
    targetPath = 'F:/20news-18828_Processed'
    targetPath2 = 'F:/20news-18828_CharacteristicWord'
    
    dataProcess()
    dictionaryConstruction()
    characteristicWordFilter()
    createTestSet()
    naiveBayesProcess()
    computeAccuracy()
    
    ##print("end main")