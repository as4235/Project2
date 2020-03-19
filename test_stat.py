from readcsvfile import reader
import pytest
import unittest

data = reader('data.csv')

class test_stat(unittest.TestCase):

    def test_pmean(self):
        from pmean import pmean
        assert pmean(data) == 805.1

    def test_median(self):
        from median import median
        assert median(data) == 251.0

    def test_mode(self):
        from mode import mode
        assert mode(data) == '123'

    def test_popstddev(self):
        from popstddev import popstddev
        assert popstddev(data) == 1631.8995342851226

    def test_variancepopprop(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) ==  1034.497285714286

    def test_zscore(self):
        from zscore import zscore
        assert zscore(data) == 1631.8995342851226

    def test_stdscore(self):
        from stdscore import stdscore
        assert stdscore(data) == 1631.8995342851226

