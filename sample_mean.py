from readcsvfile import reader
import math

data = reader('data.csv')


def SampMean(data):
        if len(data) == 0:
                return 0
        data = int(data)
        smean = sum(data) / len(data)
        sum = int(sum)
        return smean

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print(SampMean(data))
