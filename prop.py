from readcsvfile import reader
dataSet = reader('data.csv')


def prop(dataset):
    if len(dataSet) == 0:
        return 0
    
    sum_of_dataset = sum(dataSet)
    if sum_of_dataset == 0:
        return 0
    
    return dataset[0]/ sum_of_dataset


