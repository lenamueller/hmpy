from enum import Enum
import statistics
from collections import Counter


class Status(Enum):
    RAW = 0
    READY = 1


class Mean(Enum):
    ARITHMETIC = 0
    GEOMETRIC = 1
    EXPONENTIAL = 2
    HARMONIC = 3
    MEDIAN = 4


class NumericalList:

    def __init__(self, input: list[float], status: Status = Status.RAW):
        """Constructor

        Args:
            input (list[float]): numerical values
            status (Status, optional): Status of the NumericalList,
                which can be set or turned to Status.READY, if the
                data is been cleaned. Defaults to Status.RAW.
        """
        self.input: list[float] = input
        self.status: Status = status

        if not self.status.value:
            raise ValueError("Status of NumericalList object is not READY!")

    def set_status_ready(self):
        """Change status of input list."""
        self.status = Status.READY

    def mean(self, formula: Mean, m: float = None):
        """Returns the mean according the the formula.
        Possible types are:

        - Mean.ARITHMETIC
        - Mean.GEOMETRIC
        - Mean.HARMONIC
        - Mean.MEDIAN
        - Mean.EXPONENTIAL

        Args:
            formula (Mean): mean formula
            m (float): exponent for formula=Mean.EXPONENTIAL

        Returns:
            float: mean value
        """
        match formula:
            case Mean.ARITHMETIC:
                return sum(self.input)/len(self.input)

            case Mean.GEOMETRIC:
                return statistics.geometric_mean(self.input)

            case Mean.HARMONIC:
                return statistics.harmonic_mean(self.input)

            case Mean.MEDIAN:
                return statistics.median(self.input)

            case Mean.EXPONENTIAL:
                n = len(self.input)
                return (sum([x**m for x in self.input])/n)**(1/m)

    def mode(self):
        """Returns a list with a single or multiple modes of an
        input list of float numbers.

        Returns:
            list: mode(s)
        """
        c = Counter(self.input)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]

    def range(self):
        """Returns the range of an input list of float numbers.

        Returns:
            float: range
        """
        return (max(self.input)-min(self.input))

    def stdev(self, biased: bool):
        """Returns biased or unbiased standard deviation of an input
        list of float numbers.

        Args:
            biased (bool): with or without bias correction

        Returns:
            float: standard deviation
        """
        n = len(self.input)
        mean = self.mean(formula=Mean.ARITHMETIC)
        deviation_squared = [(x-mean)**2 for x in self.input]

        match biased:
            case True:
                return (sum(deviation_squared)/n)**(1/2)
            case False:
                return (sum(deviation_squared)/(n-1))**(1/2)

    def var(self, biased: bool):
        """Returns biased or unbiased variance of an input list
        of float numbers.

        Args:
            biased (bool): with or without bias correction

        Returns:
            float: variance
        """
        n = len(self.input)
        mean = self.mean(formula=Mean.ARITHMETIC)
        deviation_squared = [(x-mean)**2 for x in self.input]

        match biased:
            case True:
                return sum(deviation_squared)/n
            case False:
                return sum(deviation_squared)/(n-1)

    def skewness(self, biased: bool):
        """Returns biased or unbiased skewness of an input list
        of float numbers.

        Args:
            biased (bool): with or without bias correction

        Returns:
            float: skewness
        """
        n = len(self.input)
        mean = self.mean(formula=Mean.ARITHMETIC)
        stdev = self.stdev(biased=True)
        deviation_3 = [(x-mean)**3 for x in self.input]

        match biased:
            case True:
                return sum(deviation_3)/(n*stdev**3)
            case False:
                return sum(deviation_3)/(n*stdev**3)*(n*n)/((n-1)*(n-2))
