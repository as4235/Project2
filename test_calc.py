from calc import calc
import pytest
import unittest


class test_StaticCalc(unittest.TestCase):
    
    
    def test_add(self):
        assert calc.add(1,1) == 2

    def test_add_fail(self):
        assert calc.add(1,1) != 3

    def test_sub(self):
        assert calc.sub(2,2) == 0

    def test_sub_fail(self):
        assert calc.sub(3,1) != 1

    def test_mul(self):
        assert calc.mul(2,5) == 10

    def test_mul_fail(self):
        assert calc.sub(3,6) != 9

    def test_div(self):
        assert calc.div(2,2) == 1

    def test_div_fail(self):
        assert calc.div(3,1) != 1

    def test_rt(self):
        assert calc.rt(4) == 2

    def test_rt_fail(self):
        assert calc.rt(9) != 1
