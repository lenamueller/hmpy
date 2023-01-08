from enum import Enum
import numpy as np
import statistics
from collections import Counter


class Status(Enum):
    RAW = 0
    READY = 1


class EstimateLocation(Enum):
    ARITHMETIC_MEAN = 0
    WEIGHTED_ARITHMETIC_MEAN = 1
    TRIMMED_ARITHMETIC_MEAN = 2
    GEOMETRIC_MEAN = 3
    EXPONENTIAL_MEAN = 4
    HARMONIC_MEAN = 5
    MEDIAN = 6
    WEIGHTED_MEDIAN = 7
    PERCENTILE = 8


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

    def estimate_of_location(
            self,
            formula: EstimateLocation,
            trim_p: int = 0,
            weights: list[float] = [],
            m: float = None,
            per: int = None
            ):
        """Returns the mean according the the formula.
        Possible types are:

        EstimateLocation.ARITHMETIC_MEAN
        EstimateLocation.WEIGHTED_ARITHMETIC_MEAN
        EstimateLocation.TRIMMED_ARITHMETIC_MEAN
        EstimateLocation.GEOMETRIC_MEAN
        EstimateLocation.EXPONENTIAL_MEAN
        EstimateLocation.HARMONIC_MEAN
        EstimateLocation.MEDIAN
        EstimateLocation.WEIGHTED_MEDIAN
        EstimateLocation.PERCENTILE

        Args:
            formula (EstimateLocation): mean formula
            trim_p (int): number of smallest and largest elements
                from the numerical list which will be ignored
                (TRIMMED_ARITHMETIC_MEAN)
            weights (list[float]): element-wise weights
                (WEIGHTED_ARITHMETIC_MEAN, WEIGHTED_MEDIAN)
            m (float): exponent for formula=Mean.EXPONENTIAL
            per (int): percentile

        Returns:
            float: mean value
        """

        match formula:
            case EstimateLocation.ARITHMETIC_MEAN:
                return sum(self.input)/len(self.input)

            case EstimateLocation.TRIMMED_ARITHMETIC_MEAN:
                trimmed = sorted(self.input)[trim_p:-trim_p]
                return sum(trimmed)/len(trimmed)

            case EstimateLocation.WEIGHTED_ARITHMETIC_MEAN:
                return sum(np.multiply(self.input, weights))/sum(weights)

            case EstimateLocation.GEOMETRIC_MEAN:
                return statistics.geometric_mean(self.input)

            case EstimateLocation.HARMONIC_MEAN:
                return statistics.harmonic_mean(self.input)

            case EstimateLocation.EXPONENTIAL_MEAN:
                n = len(self.input)
                return (sum([x**m for x in self.input])/n)**(1/m)

            case EstimateLocation.MEDIAN:
                return statistics.median(self.input)

            case EstimateLocation.WEIGHTED_MEDIAN:
                weighted_list = []
                for i in range(len(self.input)):
                    weighted_list.extend([self.input[i]]*weights[i])
                return statistics.median(weighted_list)

            case EstimateLocation.PERCENTILE:
                return np.percentile(self.input, per)

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
        mean = self.estimate_of_location(
            formula=EstimateLocation.ARITHMETIC_MEAN)
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
        mean = self.estimate_of_location(
            formula=EstimateLocation.ARITHMETIC_MEAN)
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
        mean = self.estimate_of_location(
            formula=EstimateLocation.ARITHMETIC_MEAN)
        stdev = self.stdev(biased=True)
        deviation_3 = [(x-mean)**3 for x in self.input]

        match biased:
            case True:
                return sum(deviation_3)/(n*stdev**3)
            case False:
                return sum(deviation_3)/(n*stdev**3)*(n*n)/((n-1)*(n-2))
