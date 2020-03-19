from readcsvfile import reader

data = reader('data.csv')


def variancepopprop(data):
    sum = 0
    total = 0
    v = 0
    for line in data:
        line = int(line)
        total = total + line
    mean = total / len(data)
    v += ((mean - line) ** 2)
    variance = v / float(len(data))
    return variance