from readcsvfile import reader

data = reader('data.csv')

def median(data):
    n = len(data)
    data.sort()

    if n % 2 == 0:
        median1 = data[n // 2]
        median2 = data[n // 2 - 1]
        median1 = int(median1)
        median2 = int(median2)
        return (median1 + median2) / 2
    else:
        return data[n // 2]
