from FileReader import readCSV
data = readCSV('data.csv')


def Proportion(data):
    if len(data) == 0:
        return 0
    
    result = []
    sum_of_dataset = sum(data)
    if sum_of_dataset == 0:
        return 0
    
    for datas in data:
        result.append(datas/sum_of_dataset)

    return result

#dataSet = [1,2,3,4,5,6,7,8,9,10]
print (Proportion(data))
