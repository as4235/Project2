from readcsvfile import reader

data = reader('data.csv')


def popstddev(data):
    sum = 0
    total = 0
    for line in data:
        line = int(line)
        total = total + line
    mean = total / len(data)
    for line in data:
        line = int(line)
        sum += (line - mean) ** 2
        popstddev = (sum / len(data) - 1) ** 0.5
    return popstddev