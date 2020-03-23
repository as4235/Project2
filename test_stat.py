from readcsvfile import reader
import pytest
import unittest
testData = [1,2,3]

data = reader('data.csv')

class test_stat(unittest.TestCase):

    def test_pmean(self):
        from pmean import pmean
        assert pmean(data) == 462.0285714285714

    def test_pmean_fail(self):
        from pmean import pmean
        assert pmean(data) != 80

    def test_median(self):
        from median import median
        assert median(data) == 235.5

    def test_median_fail(self):
        from median import median
        assert median(data) != 25

    def test_mode(self):
        from mode import mode
        assert mode(data) == '1'

    def test_mode_fail(self):
        from mode import mode
        assert mode(data) != '23'

    def test_popstddev(self):
        from popstddev import popstddev
        assert popstddev(data) == 1347.0801868648168

    def test_popstddev_fail(self):
        from popstddev import popstddev
        assert popstddev(data) != 16

    def test_variancepopprop(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) == 8.381025000000026

    def test_variancepopprop_fail(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) !=  1

    def test_zscore(self):
        from zscore import zscore
        assert zscore(data) == 1436.6279228667147

    def test_zscore_fail(self):
        from zscore import zscore
        assert zscore(data) != 16

    def test_stdscore(self):
        from stdscore import stdscore
        assert stdscore(data) == 1384.8464158727334

    def test_stdscore_fail(self):
        from stdscore import stdscore
        assert stdscore(data) != 16
 
