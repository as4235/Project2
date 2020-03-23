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
        assert popstddev(data) == 1631.8995342851226

    def test_popstddev_fail(self):
        from popstddev import popstddev
        assert popstddev(data) != 16

    def test_variancepopprop(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) ==  1034.497285714286

    def test_variancepopprop_fail(self):
        from variancepopprop import variancepopprop
        assert variancepopprop(data) !=  1

    def test_zscore(self):
        from zscore import zscore
        assert zscore(data) == 1631.8995342851226

    def test_zscore_fail(self):
        from zscore import zscore
        assert zscore(data) != 16

    def test_stdscore(self):
        from stdscore import stdscore
        assert stdscore(data) == 1631.8995342851226

    def test_stdscore_fail(self):
        from stdscore import stdscore
        assert stdscore(data) != 16
 
# confidence interval
    def test_calc_confidenceInterval(self):
        from confidence_interval import confidenceInterval
        assert confidenceInterval(testData) == 1.076

    def test_calc_confidenceInterval_fail(self):
        from confidence_interval import confidenceInterval
        assert confidenceInterval(testData) != 5
 

# Population variance
    def test_calc_variance(self):
        from population_variance import pop_variance
        assert variance(data) == variance(data)

    def test_calc_variance_fail(self):
        from population_variance import pop_variance
        assert variance(data) != 2
        
        
 #Sample Mean 
    def test_calc_sampleMean(self):
        from sample_mean import SampMean
        assert SampMean(testData) == 2

    def test_calc_sampleMean_fail(self):
        from sample_mean import SampMean
        assert SampMean(testData) != 1
       
  
# Sample Standard deviation 
    def test_calc_std(self):
        from sample_SD import sample_standardDeviation
        assert sample_standardDeviation(data) == sample_standardDeviation(data)

    def test_calc_std_fail(self):
        from StatisticsModule import standardDeviation
        assert sample_standardDeviation(data) != 2
    
    
  # Variance of sample proportion
    def test_calc_varianceSampleProportion(self):
        from variance_of_sample_proportion import VSP
        assert VSP(testData) == 1

    def test_calc_varianceSampleProportion_fail(self):
        from variance_of_sample_proportion import VSP
        assert VSP(testData) != 2

   
# Correlation Coefficient
# Proportion

