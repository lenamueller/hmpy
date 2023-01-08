import sys

sys.path.insert(1, 'analysis')
print(sys.path)
from numericallist import NumericalList, Status, \
    EstimateLocation, EstimateVariability


# -------------------------------------------------------------------------
# estimates of location
# -------------------------------------------------------------------------

def test_arithmetic_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 6/3 == bs.estimate_of_location(
        formula=EstimateLocation.ARITHMETIC_MEAN)


def test_weighted_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.0 == bs.estimate_of_location(
        formula=EstimateLocation.WEIGHTED_ARITHMETIC_MEAN, weights=[2, 2, 2])


def test_trimmed_arithmetic_mean():
    bs = NumericalList(input=[1, 2, 3, 4], status=Status.READY)
    assert 5/2 == bs.estimate_of_location(
        formula=EstimateLocation.TRIMMED_ARITHMETIC_MEAN, trim_p=1)


def test_geometric_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1.8171 == round(bs.estimate_of_location(
        formula=EstimateLocation.GEOMETRIC_MEAN), 4)


def test_exponential_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.1602 == round(bs.estimate_of_location(
        formula=EstimateLocation.EXPONENTIAL_MEAN, m=2), 4)


def test_harmonic_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1.6364 == round(bs.estimate_of_location(
        formula=EstimateLocation.HARMONIC_MEAN), 4)


def test_median_even():
    bs = NumericalList(input=[1, 2, 3, 4], status=Status.READY)
    assert 2.5 == bs.estimate_of_location(formula=EstimateLocation.MEDIAN)


def test_median_odd():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.0 == bs.estimate_of_location(formula=EstimateLocation.MEDIAN)


def test_weighted_median_even():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.5 == bs.estimate_of_location(
        formula=EstimateLocation.WEIGHTED_MEDIAN, weights=[1, 2, 3])


def test_weighted_median_odd():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 3.0 == bs.estimate_of_location(
        formula=EstimateLocation.WEIGHTED_MEDIAN, weights=[1, 1, 3])


def test_percentile():
    bs = NumericalList(input=range(1, 12, 1), status=Status.READY)
    assert 6.0 == bs.estimate_of_location(
        formula=EstimateLocation.PERCENTILE, per=50)
    assert bs.estimate_of_location(
        formula=EstimateLocation.MEDIAN) == bs.estimate_of_location(
            formula=EstimateLocation.PERCENTILE, per=50)

# -------------------------------------------------------------------------
# estimates of variability
# ------------------------------------------------------------------------


def test_avg_absolute_deviation_mean():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.estimate_of_variability(
        formula=EstimateVariability.AVG_ABSOLUTE_DEVIATION_MEAN)


def test_avg_absolute_deviation_mean_2():
    bs = NumericalList(input=[1, 1, 1], status=Status.READY)
    assert 0.0 == bs.estimate_of_variability(
        formula=EstimateVariability.AVG_ABSOLUTE_DEVIATION_MEAN)


def test_avg_absolute_deviation_median_1():
    bs = NumericalList(input=[1, 1, 3], status=Status.READY)
    assert 2/3 == bs.estimate_of_variability(
        formula=EstimateVariability.AVG_ABSOLUTE_DEVIATION_MEDIAN)


def test_avg_absolute_deviation_median_2():
    bs = NumericalList(input=[1, 1, 1], status=Status.READY)
    assert 0.0 == bs.estimate_of_variability(
        formula=EstimateVariability.AVG_ABSOLUTE_DEVIATION_MEDIAN)


def test_mean_absolute_deviation():
    bs = NumericalList(input=[1, 1, 2, 2, 4, 6, 9], status=Status.READY)
    assert 1.0 == bs.estimate_of_variability(
        formula=EstimateVariability.MEDIAN_ABSOLUTE_DEVIATION)


def test_variance_biased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.estimate_of_variability(
        formula=EstimateVariability.VARIANCE, biased=True)


def test_variance_unbiased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1/1 == bs.estimate_of_variability(
        formula=EstimateVariability.VARIANCE, biased=False)


def test_stdev_biased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert (2/3)**(1/2) == bs.estimate_of_variability(
        formula=EstimateVariability.STDEV, biased=True)


def test_stdev_unbiased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1/1 == round(bs.estimate_of_variability(
        formula=EstimateVariability.STDEV, biased=False), 4)


def test_range():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2.0 == bs.estimate_of_variability(
        formula=EstimateVariability.RANGE)


def test_iqr():
    bs = NumericalList(input=[1, 2, 3, 3, 5, 6, 7, 9], status=Status.READY)
    assert 4.0 == bs.estimate_of_variability(formula=EstimateVariability.IQR)


def test_mode_single():
    bs = NumericalList(input=[1, 3, 3], status=Status.READY)
    assert [3] == bs.mode()


def test_mode_multiple():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert [1, 2, 3] == bs.mode()


# -------------------------------------------------------------------------
# distribution
# -------------------------------------------------------------------------

def test_skewness_biased():
    bs = NumericalList(input=[1, 1, 1, 5], status=Status.READY)
    assert 1.1547 == round(bs.skewness(biased=True), 4)


def test_skewness_unbiased():
    bs = NumericalList(input=[1, 1, 1, 5], status=Status.READY)
    assert 3.0792 == round(bs.skewness(biased=False), 4)
