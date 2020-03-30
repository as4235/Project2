from readcsvfile import reader
import math

dataSet = reader('data.csv')

def sstddev(dataSet):
    mean = sum(dataSet[:5]) / 5
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet[:5]])/(5))

    return std

