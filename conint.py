from readcsvfile import reader
from scipy.stats import sem, t
from scipy import mean
confidence = 0.95

dataSet = reader('data.csv')

def conint(dataSet):
        n = len(dataSet)
        m = sum(dataSet)/len(dataSet)
        std_err = sem(dataSet)
        h = std_err * t.ppf((1 + confidence) / 2, n - 1)

        start = m + h
        end = m - h
        return ([start, end])

