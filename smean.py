from readcsvfile import reader
import math

dataSet = reader('data.csv')


def smean(dataSet):
        if len(dataSet) == 0:
                return 0
        smean = sum(dataSet[:5]) / 5

        return smean
