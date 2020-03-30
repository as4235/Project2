from readcsvfile import reader
import math

dataSet = reader('data.csv')

def popvar(dataSet):
    if len(dataSet) == 0:
        return 0
    
    cal_mean = sum(dataSet) / len(dataSet)
    
    variance = sum((data - cal_mean) ** 2 for data in dataSet) / len(dataSet)
    return variance

