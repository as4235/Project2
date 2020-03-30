from readcsvfile import reader
import pytest
import unittest
testData = [1,2,3]

data = reader('data.csv')

class test_stat(unittest.TestCase):
    def test_popcorcoeff(self):
        from popcorcoeff import popcorcoeff
        assert popcorcoeff(data, data) == 0.9722222222222224
    def test_conint(self):
        from conint import conint
        assert conint(data) == [1758.1902724304498, 18.476394236216947]
        
    def test_popvar(self):
        from popvar import popvar
        assert popvar(data) == 2889718.8888888876
        
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
        
    
               