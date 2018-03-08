#<--*-- coding:utf-8 --*-->
from numpy.ma import zeros
from numpy import *

#归一化特征值
def autoNorm(DataSet):
    #公式：newValues = (oldValues - min)/(max-min)
    minValues = DataSet.min(0)
    maxValues = DataSet.max(0)
    ranges = maxValues - minValues
    NormData = zeros(DataSet.shape())
    m = DataSet.shape[0]
    NormData = DataSet - tile(minValues,(m,1))
    NormData = NormData/tile(ranges,(m,1))
    return NormData,ranges,minValues
#文本文件转换成NumPy的解析程序
def FileToMatrix(filename):
    fr = open(filename)
    Filedata = fr.readlines()
    Lines = len(Filedata)
    NumCh = 3#characteristic 's number
    DataMat = zeros((Lines,NumCh))
    #根据情况处理