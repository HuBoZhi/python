#<--*-- coding:utf-8 --*-->
from KNN import *
from DecisionTree import *
from bayes import *
from Logistic import *

if __name__=="__main__":
    print("hello world")
    dataArr,labelMat = loadDataSet()
    weight = gradAscent(dataArr,labelMat)
    plotBestFit(weight.getA())
