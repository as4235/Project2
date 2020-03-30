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
        assert median(data) == 8.0

    def test_median_fail(self):
        from median import median
        assert median(data) != 25

    def test_mode(self):
        from mode import mode
        assert mode(data) == 1.0

    def test_mode_fail(self):
        from mode import mode
        assert mode(data) != '23'

    def test_popstddev(self):
        from popstddev import popstddev
        assert popstddev(data) == 1413.767041453435

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
        assert zscore(data) == 1519.291890889379

    def test_zscore_fail(self):
        from zscore import zscore
        assert zscore(data) != 16

    def test_stdscore(self):
        from stdscore import stdscore
        assert stdscore(data) == 1384.8464158727334

    def test_stdscore_fail(self):
        from stdscore import stdscore
        assert stdscore(data) != 16
 
    def test_popcorcoeff(self):
        from popcorcoeff import popcorcoeff
        assert popcorcoeff(data, data) == 0.9888888888888889 
        
        
    def test_popvar(self):
        from popvar import popvar
        assert popvar(data) == 0.00017951815835750415
        
    def test_prop(self):
        from prop import prop
        assert prop(data) == 0.002564102564102564
        
    def test_smean(self):
        from smean import smean
        assert smean(data) == 196.0
        
    def test_sstddev(self):
        from sstddev import sstddev
        assert sstddev(data) == 188.84702804121648
        
    def test_vsampprop(self):
        from vsampprop import vsampprop
        assert vsampprop(data) == 0.0005581277829308491
