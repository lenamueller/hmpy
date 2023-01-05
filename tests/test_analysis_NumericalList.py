import sys

sys.path.insert(1, 'analysis')
print(sys.path)
from numericallist import NumericalList, Mean, Status


def test_mean_arithmetic():
    num_list = [1, 2, 3]
    bs = NumericalList(input=num_list, status=Status.READY)
    assert 6/3 == bs.mean(formula=Mean.ARITHMETIC)


def test_mean_geometric():
    num_list = [1, 2, 3]
    bs = NumericalList(input=num_list, status=Status.READY)
    assert 1.8171 == round(bs.mean(formula=Mean.GEOMETRIC), 4)


def test_mean_exponential():
    num_list = [1, 2, 3]
    bs = NumericalList(input=num_list, status=Status.READY)
    assert 2.1602 == round(bs.mean(formula=Mean.EXPONENTIAL, m=2), 4)


def test_mean_harmonic():
    num_list = [1, 2, 3]
    bs = NumericalList(input=num_list, status=Status.READY)
    assert 1.6364 == round(bs.mean(formula=Mean.HARMONIC), 4)


def test_mean_median_even():
    num_list = [1, 2, 3, 4]
    bs = NumericalList(input=num_list, status=Status.READY)
    assert 2.5 == bs.mean(formula=Mean.MEDIAN)


def test_mean_median_odd():
    num_list = [1, 2, 3]
    bs = NumericalList(input=num_list, status=Status.READY)
    assert 2.0 == bs.mean(formula=Mean.MEDIAN)


def test_mode_single():
    bs = NumericalList(input=[1, 3, 3], status=Status.READY)
    assert [3] == bs.mode()


def test_mode_multiple():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert [1, 2, 3] == bs.mode()


def test_range():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2 == bs.range()


def test_stdev_biased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert (2/3)**(1/2) == bs.stdev(biased=True)


def test_stdev_unbiased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1/1 == round(bs.stdev(biased=False), 4)


def test_var_biased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 2/3 == bs.var(biased=True)


def test_var_unbiased():
    bs = NumericalList(input=[1, 2, 3], status=Status.READY)
    assert 1/1 == bs.var(biased=False)


def test_skewness_biased():
    bs = NumericalList(input=[1, 1, 1, 5], status=Status.READY)
    assert 1.1547 == round(bs.skewness(biased=True), 4)


def test_skewness_unbiased():
    bs = NumericalList(input=[1, 1, 1, 5], status=Status.READY)
    assert 3.0792 == round(bs.skewness(biased=False), 4)
