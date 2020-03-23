from FileReader import readCSV
import math

data = readCSV('data.csv', nrows = 10)

def sample_standardDeviation(data):
    mean = sum(data) / len(data)
    std = math.sqrt(sum([(val - mean)**2 for val in data])/(len(data) - 1))

    return std

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (sample_standardDeviation(data))
