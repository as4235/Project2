from FileReader import readCSV

confidence = 0.95

dataSet = readCSV('data.csv')

def confidenceInterval(dataSet):
    a = len(dataSet)
    b = sum(dataSet) / a
    std = math.sqrt(sum([(val - b)**2 for val in dataSet])/(len(dataSet) - 1))
    std_err = std / math.sqrt(a)
    t = b / std_err
    h = std_err * t * float(1 + confidence) / float(2., a - 1)

    start = b + h
    end = b - h
    
    return start, end

    print ("Confidence Interval is:", start, end)
