from readcsvfile import reader
import pytest
import unittest
testData = [1,2,3]

data = reader('data.csv')

class test_stat(unittest.TestCase):

    def test_pmean(self):
        from pmean import pmean
        assert pmean(data) == 805.1

    def test_pmean_fail(self):
        from pmean import pmean
        assert pmean(data) != 80

    def test_median(self):
        from median import median
        assert median(data) == 251.0

    def test_median_fail(self):
        from median import median
        assert median(data) != 25

    def test_mode(self):
        from mode import mode
        assert mode(data) == '123'

    def test_mode_fail(self):
        from mode import mode
        assert mode(data) != '23'

    def test_popstddev(self):
        from popstddev import popstddev
        assert popstddev(data) == 1631.899534285123

    def test_popstddev_fail(self):
        from popstddev import popstddev
        assert popstddev(data) != 16

    def test_variancepopprop(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) == 482.76540000000006

    def test_variancepopprop_fail(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) !=  1

    def test_zscore(self):
        from zscore import zscore
        assert zscore(data) == 1631.8995342851235

    def test_zscore_fail(self):
        from zscore import zscore
        assert zscore(data) != 16

    def test_stdscore(self):
        from stdscore import stdscore
        assert stdscore(data) == 1631.8995342851233

    def test_stdscore_fail(self):
        from stdscore import stdscore
        assert stdscore(data) != 16
 
