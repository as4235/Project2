from FileReader import readCSV
import math

dataSet = readCSV('data.csv', nrows = 10)


def SampMean(dataSet):
        if len(dataSet) == 0:
                return 0
        smean = sum(dataSet) / len(dataSet)

        return smean

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print(SampMean(dataSet))
