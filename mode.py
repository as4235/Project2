from readcsvfile import reader

data = reader('data.csv')


def mode(data):
    max_count = (0, 0)
    for num in data:
        occurences = data.count(num)
        if occurences > max_count[0]:
            max_count = (occurences, num)
    return max_count[1]
