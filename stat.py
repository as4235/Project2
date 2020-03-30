from readcsvfile import reader
data = reader('data.csv')
if __name__ == "__main__":
    print(
        "1.Population Mean 2. Median 3. Mode 4. Population Standard Deviation 5. Variance of population proportion 6. "
        "Z-Score 7. Standardized score 8. Population Correlation Coefficient 9. Confidence Interval 10. Population "
        "Variance 11. P Value 12. Proportion 13. Sample Mean 14. Sample Standard Deviation 15. Variance of sample "
        "proportion")
    c = int(input())
    if c == 1:
        from pmean import pmean
        print((pmean(data)))
    elif c == 2:
        from median import median

        print(str(median(data)))
    elif c == 3:
        from mode import mode

        print(str(mode(data)))
    elif c == 4:
        from popstddev import popstddev

        print(str(popstddev(data)))
    elif c == 5:
        from variancepopprop import variancepopprop

        print(str(variancepopprop(data)))
    elif c == 6:
        from zscore import zscore

        print(str(zscore(data)))
    elif c == 7:
        from stdscore import stdscore
        print(float(stdscore(data)))
    elif c == 8:
        from popcorcoeff import popcorcoeff
        print(float(popcorcoeff(data)))
    elif c == 9:
        from conint import conint
        print (conint(data))
    elif c == 10:
        from popvar import popvar
        print(popvar(data))
    elif c == 11:
        from pval import pval
        print(pval(data))
    elif c == 12:
        from prop import prop
        print((prop(data)))
    elif c == 13:
        from smean import smean
        print((smean(data)))
    elif c == 14:
        from sstddev import sstddev
        print((sstddev(data)))
    elif c == 15:
        from vsampprop import vsampprop
        print((vsampprop(data)))
    else:
        print("error")
