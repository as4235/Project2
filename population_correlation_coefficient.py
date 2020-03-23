import math
from FileReader import readCSV

x = readCSV("xvalues.csv")
y= readCSV("yvalues.csv")

def population_corelation_coefficient(x,y):
    if len(x) == 0 or len(y) == 0 or len(x) != len(y):
        return 0
    s = 0
    x_mean = sum(x)/len(x)
    y_mean = sum(y)/len(y)
    x_SD = math.sqrt(sum([(val - x_mean)**2 for val in x])/(len(x) - 1))
    y_SD = math.sqrt(sum([(val - y_mean)**2 for val in y])/(len(y) - 1))
    for i, j in zip(x,y):
        s = s + (((i-x_mean)/x_SD)*((j-y_mean)/y_SD))
    return s/len(x)


print (population_corelation_coefficient(x,y))	
