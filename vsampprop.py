from readcsvfile import reader
import math

dataset = reader('data.csv')

def vsampprop(dataset):
    if len(dataset) == 0:
        result = 0

    sum_of_dataset = sum(dataset)
    if sum_of_dataset == 0:
        result = 0

    result = []
    for data in dataset:
        result.append(data/sum_of_dataset)

    cal_mean = sum(result) / len(result)
    cal_variance = sum((xi - cal_mean) ** 2 for xi in result) / len(result)
    return cal_variance


