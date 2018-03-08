#<--*-- coding:utf-8 --*-->
from math import log
from numpy import *
####################################### 决策树 #########################################
#计算给数据集的香农熵:熵越高，信息增益越高，信息增益最高的特征(的集合)就是最好的选择
def CaclShannonEnt(dataSet):
    Datanum = len(dataSet)
    dataDict = {}
    for data in dataSet:
        Current = data[-1]
        if Current not in dataDict.keys():
            dataDict[Current] = 0
        dataDict[Current] += 1
    ShannonEnt = 0.0
    for key in dataDict:
        prob = float(dataDict[key])/Datanum
        ShannonEnt -= prob*log(prob,2)
    return ShannonEnt
#按照给定特征划分数据集
def SplitDataSet(dataSet,axis,value):#三个参数分别为待划分的数据集，划分数据集的特征，需要返回的特征的值
    retDataSet = []
    for featVec in dataSet:
        # 找到特征的值满足value的数据集，去除此特征对应的数据，生成一个新的没有此次划分数据集的特征的新数据集
        if featVec[axis] == value:
            surData = featVec[:axis]
            surData.extend(featVec[axis+1:])
            retDataSet.append(surData)
    return retDataSet
#选择最好的数据集划分方式
def ChooseBestFeatureToSplit(dataSet):
    numFearures = len(dataSet[0]) - 1
    baseEtropy = CaclShannonEnt(dataSet)
    bestInfoGain = 0.0;bestFearure = -1
    for i in range(numFearures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = SplitDataSet(dataSet,i,value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * CaclShannonEnt(subDataSet)
        infoGain = baseEtropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFearure = i
    return bestFearure
#表决函数
def  MajorityCnt(classList):
    classCount = {}
    for vote in classCount:
        if vote not in classCount.keys():classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(),key = operator.itemgetter(1),reverse = True)
    return sortedClassCount[0][0]
#创建树的函数
def CreateTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return MajorityCnt(classList)
    bestFeat = ChooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueValues = set(featValues)
    for value in uniqueValues:
        subLables = labels[:]
        myTree[bestFeatLabel][value] = CreateTree(SplitDataSet(dataSet,bestFeat,value),subLables)
    return myTree
#使用决策树的分类函数
def UseDecisionTree(tree,featLabels,testVec):
    global classLabel
    firstStr = list(tree.keys())[0]
    secondDict = tree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = UseDecisionTree(secondDict[key],featLabels,testVec)
            else:
                classLabel = secondDict[key]
    return classLabel
#存储决策树
def storeTree(Decisiontree,filename):
    import pickle
    fw = open(filename,'w')
    pickle.dump(Decisiontree,fw)
    fw.close()
#提取决策树
def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
#创建数据集
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels