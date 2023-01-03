import sys
import statistics

sys.path.insert(1, 'analysis')
print(sys.path)
from numericallist import NumericalList


def test_mean_arithmetic():
    num_list = [1, 2, 3, 4, 5, 6]
    bs = NumericalList(input=num_list)
    assert statistics.mean(num_list) == bs.mean_arithmetic()


def test_mean_geometric():
    num_list = [1, 2, 3, 4, 5, 6]
    bs = NumericalList(input=num_list)
    assert statistics.geometric_mean(num_list) == bs.mean_geometric()


def test_mean_exponential():
    num_list = [1, 2, 3]
    bs = NumericalList(input=num_list)
    assert 2.1602 == round(bs.mean_exponential(m=2), 4)


def test_mean_harmonic():
    num_list = [1, 2, 3, 4, 5, 6]
    bs = NumericalList(input=num_list)
    assert statistics.harmonic_mean(num_list) == bs.mean_harmonic()


def test_mean_median_even():
    num_list = [1, 2, 3, 4, 5, 6]
    bs = NumericalList(input=num_list)
    assert statistics.median(num_list) == bs.mean_median()


def test_mean_median_odd():
    num_list = [1, 2, 3, 4, 5]
    bs = NumericalList(input=num_list)
    assert statistics.median(num_list) == bs.mean_median()


def test_mode_single():
    bs = NumericalList(input=[1, 3, 3])
    assert [3] == bs.mode()


def test_mode_multiple():
    bs = NumericalList(input=[1, 2, 3])
    assert [1, 2, 3] == bs.mode()


def test_range():
    bs = NumericalList(input=[1, 2, 3])
    assert 2 == bs.range()


def test_stdev_biased():
    bs = NumericalList(input=[1, 2, 3])
    assert (2/3)**(1/2) == bs.stdev(biased=True)


def test_stdev_unbiased():
    bs = NumericalList(input=[1, 2, 3])
    assert 1/1 == round(bs.stdev(biased=False), 4)


def test_var_biased():
    bs = NumericalList(input=[1, 2, 3])
    assert 2/3 == bs.var(biased=True)


def test_var_unbiased():
    bs = NumericalList(input=[1, 2, 3])
    assert 1/1 == bs.var(biased=False)


def test_skewness_biased():
    bs = NumericalList(input=[1, 1, 1, 5])
    assert 1.1547 == round(bs.skewness(biased=True), 4)


def test_skewness_unbiased():
    bs = NumericalList(input=[1, 1, 1, 5])
    assert 3.0792 == round(bs.skewness(biased=False), 4)
