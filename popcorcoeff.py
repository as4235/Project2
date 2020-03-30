from readcsvfile import reader
import math

data1 = reader('data.csv')
data2 = reader('data.csv')

def popcorcoeff(data1, data2):
    if len(data1) == 0 or len(data2) == 0 or len(data1) != len(data2):
        return 0
    s = 0
    data1_mean = sum(data1)/len(data2)
    data2_mean = sum(data2)/len(data2)
    data1_SD = math.sqrt(sum([(val - data1_mean)**2 for val in data1])/(len(data1) - 1))
    data2_SD = math.sqrt(sum([(val - data2_mean)**2 for val in data2])/(len(data2) - 1))
    for i, j in zip(data1,data2):
        s = s + (((i-data1_mean)/data1_SD)*((j-data2_mean)/data2_SD))
    return s/len(data1)