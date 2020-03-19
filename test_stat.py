from readcsvfile import reader
import pytest
import unittest

data = reader('test.csv')

class test_stat(unittest.TestCase):

    def test_pmean(self):
        from pmean import pmean
        assert pmean(data) == 604.975

    def test_median(self):
        from median import median
        assert median(data) == 235.5

    def test_mode(self):
        from mode import mode
        assert mode(data) == '123'

    def test_popstddev(self):
        from popstddev import popstddev
        assert popstddev(data) == 1494.3246635186076

    def test_variancepopprop(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) == 342.0764548104956

    def test_zscore(self):
        from zscore import zscore
        assert zscore(data) == 1549.2893245271362

    def test_stdscore(self):
        from stdscore import stdscore
        assert stdscore(data) == 1519.291890889378

