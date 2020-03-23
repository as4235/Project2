from FileReader import readCSV
import math

data = readCSV('data.csv')

def pop_variance(data):
    if len(data) == 0:
        return 0
    
    cal_mean = sum(data) / len(data)
    
    variance = sum((data - cal_mean) ** 2 for data in data) / len(data)
    return variance

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (pop_variance(data))
