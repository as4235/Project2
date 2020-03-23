from FileReader import readCSV
import math

dataSet = readCSV('data.csv', nrows = 10)

def sample_standardDeviation(dataSet):
    mean = sum(dataSet) / len(dataSet)
    std = math.sqrt(sum([(val - mean)**2 for val in dataSet])/(len(dataSet) - 1))

    return std

dataSet = [1,2,3,4,5,6,7,8,9,10]
print (sample_standardDeviation(dataSet))
