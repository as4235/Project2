import math
from readcsvfile import reader
data = reader('test.csv')


def test_csv_reader():
    data = reader('test.csv')
    assert len(data) == 30

def test_csv_reader_fail():
    data = reader('test.csv')
    assert len(data) != 1