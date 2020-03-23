from FileReader import readCSV
import math

dataSet = readCSV('data.csv')

def pop_variance(dataSet):
    if len(dataSet) == 0:
        return 0
    
    cal_mean = sum(dataSet) / len(dataSet)
    
    variance = sum((data - cal_mean) ** 2 for data in dataSet) / len(dataSet)
    return variance

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (pop_variance(dataSet))
