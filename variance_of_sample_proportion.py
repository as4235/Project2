from FileReader import readCSV
import math

dataset = readCSV('data.csv')

def variance_of_sample_proportion(dataset):
    if len(dataSet) == 0:
        result = 0

    sum_of_dataset = sum(dataSet)
    if sum_of_dataset == 0:
        result = 0

    result = []
    for data in dataSet:
        result.append(data/sum_of_dataset)

    cal_mean = sum(result) / len(result)
    cal_variance = sum((xi - cal_mean) ** 2 for xi in result) / len(result)
    return cal_variance

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (variance_of_sample_proportion(dataSet))
