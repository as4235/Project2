from readcsvfile import reader


data = reader('data.csv')


def pmean(data):
    total = 0
    for line in data:
        line = int(line)
        total = total + line
    mean = total / len(data)
    return mean
