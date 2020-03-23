from FileReader import readCSV
dataSet = readCSV('data.csv')


def Proportion(dataset):
    if len(dataSet) == 0:
        return 0
    
    result = []
    sum_of_dataset = sum(dataSet)
    if sum_of_dataset == 0:
        return 0
    
    for data in dataset:
        result.append(data/sum_of_dataset)

    return result

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (Proportion(dataSet))
