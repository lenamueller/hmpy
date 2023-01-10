import sys
import scipy

from hmpy.numericallist import NumericalList, Status


# -------------------------------------------------------------------------
# estimates of location
# -------------------------------------------------------------------------

def test_arithmetic_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 6/3 == bs.arithmetic_mean()


def test_weighted_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.0 == bs.weighted_arithmetic_mean(weights=[2, 2, 2])


def test_trimmed_mean():
    bs = NumericalList(input=[1, 2, 3, 4], status=Status.READY)
    assert 5/2 == bs.trimmed_mean(p=1)


def test_geometric_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1.8171 == round(bs.geometric_mean(), 4)


def test_exponential_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.1602 == round(bs.exponential_mean(m=2), 4)


def test_harmonic_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1.6364 == round(bs.harmonic_mean(), 4)


def test_median_even():
    bs = NumericalList(input=[1, 2, 3, 4], status=Status.READY)
    assert 2.5 == bs.median()


def test_median_odd():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.0 == bs.median()


def test_weighted_median_even():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.5 == bs.weighted_median(weights=[1, 2, 3])


def test_weighted_median_odd():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 3.0 == bs.weighted_median(weights=[1, 1, 3])


def test_percentile():
    bs = NumericalList(input=range(1, 12, 1), status=Status.READY)
    test = bs.percentile(per=50)
    assert 6.0 == test
    assert bs.median() == test

# -------------------------------------------------------------------------
# estimates of variability
# -------------------------------------------------------------------------


def test_avg_absolute_deviation_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.avg_absolute_deviation_from_mean()


def test_avg_absolute_deviation_mean_2():
    bs = NumericalList(input=[1, 1, 1], status=Status.READY)
    assert 0.0 == bs.avg_absolute_deviation_from_mean()


def test_avg_absolute_deviation_median_1():
    bs = NumericalList(input=[1, 1, 3], status=Status.READY)
    assert 2/3 == bs.avg_absolute_deviation_from_median()


def test_avg_absolute_deviation_median_2():
    bs = NumericalList(input=[1, 1, 1], status=Status.READY)
    assert 0.0 == bs.avg_absolute_deviation_from_median()


def test_mean_absolute_deviation():
    bs = NumericalList(input=[1, 1, 2, 2, 4, 6, 9], status=Status.READY)
    assert 1.0 == bs.median_absolute_deviaton()


def test_variance_biased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.variance(biased=True)


def test_variance_unbiased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1/1 == bs.variance(biased=False)


def test_stdev_biased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert (2/3)**(1/2) == bs.stdev(biased=True)


def test_stdev_unbiased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1/1 == round(bs.stdev(biased=False), 4)


def test_range():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.0 == bs.range()


def test_iqr():
    bs = NumericalList(input=[1, 2, 3, 3, 5, 6, 7, 9], status=Status.READY)
    assert 4.0 == bs.iqr()

def test_mu2():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.mu(k=2)

def test_mu3():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 0.0 == bs.mu(k=3)
    
def test_mu4():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.mu(k=4)

# -------------------------------------------------------------------------
# estimates of distribution
# -------------------------------------------------------------------------

def test_skewness_biased():
    bs = NumericalList(input=[1, 5, 5, 1], status=Status.READY)
    test = round(bs.coefficient_of_skewness(biased=True), 4)
    ref = round(scipy.stats.skew([1, 5, 5, 1], bias=True), 4)
    assert test == ref


def test_skewness_unbiased():
    bs = NumericalList(input=[1, 5, 5, 1], status=Status.READY)
    test = round(bs.coefficient_of_skewness(biased=False), 4)
    ref = round(scipy.stats.skew([1, 5, 5, 1], bias=False), 4)
    # assert 3.0792 == 
    assert test == ref


def test_kurtosis_biased():
    bs = NumericalList(input=[-10, -5, 0, 5, 10], status=Status.READY)
    test = round(bs.coefficient_of_kurtosis(biased=True), 4)
    ref = round(scipy.stats.kurtosis([-10, -5, 0, 5, 10], bias=True) + 3, 4)
    assert test == ref


# def test_kurtosis_unbiased():
#     bs = NumericalList(input=[-10, -5, 0, 5, 10], status=Status.READY)
#     test = round(bs.coefficient_of_kurtosis(biased=False), 4)
#     ref = round(scipy.stats.kurtosis([-10, -5, 0, 5, 10], bias=False, fisher=False) + 3, 4)
#     assert test == ref


def test_mode_single():
    bs = NumericalList(input=[1, 3, 3], status=Status.READY)
    assert [3] == bs.mode()


def test_mode_multiple():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert [1, 2, 3] == bs.mode()
