from readcsvfile import reader
import math

data = reader('data.csv')

def variance_of_sample_proportion(data):
    if len(data) == 0:
        result = 0
    sum = int(sum)
    sum_of_dataset = int(sum_of_dataset)
    sum_of_dataset = sum(data)
    if sum_of_dataset == 0:
        result = 0

    result = []
    for datas in data:
        result.append(datas/sum_of_dataset)

    cal_mean = sum(result) / len(result)
    cal_variance = sum((xi - cal_mean) ** 2 for xi in result) / len(result)
    return cal_variance

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (variance_of_sample_proportion(data))
