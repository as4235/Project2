from readcsvfile import reader
import math

data = reader('data.csv')

def sample_standardDeviation(data):
    data = int(data)
    mean = sum(data) / len(data)
    std = math.sqrt(sum([(val - mean)**2 for val in data])/(len(data) - 1))

    return std

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (sample_standardDeviation(data))
