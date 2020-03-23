from FileReader import readCSV
import math

data = readCSV('data.csv', nrows = 10)


def SampMean(data):
        if len(data) == 0:
                return 0
        smean = sum(data) / len(data)

        return smean

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print(SampMean(data))
