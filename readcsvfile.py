import csv

data = []


def reader(file):
    with open(file) as file:
        value = csv.reader(file)
        for row in value:
            row = row.pop(0)
            data.append(float(row))

    return data
