from readcsvfile import reader

import math

confidence = 0.95

data = reader('data.csv')

def confidenceInterval(data):
    a = len(data)
    b = sum(data) / a
    std = math.sqrt(sum([(val - b)**2 for val in data])/(len(data) - 1))
    std_err = std / math.sqrt(a)
    t = b / std_err
    h = std_err * t * float(1 + confidence) / float(2., a - 1)

    start = b + h
    end = b - h
    
    return start, end

    print ("Confidence Interval is:", start, end)
