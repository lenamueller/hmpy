from enum import Enum
import numpy as np
import statistics
from collections import Counter


class Status(Enum):
    RAW = 0
    READY = 1


class NumericalList:

    def __init__(self, input: list[float], status: Status = Status.RAW):
        """Constructor

        Args:
            input (list[float]): numerical values
            status (Status, optional): Status of the NumericalList,
                which can be set or turned to Status.READY, if the
                data is been cleaned. Defaults to Status.RAW.
        """
        self.data: list[float] = input
        self.status: Status = status
        self.n: int = len(input)

        if (not self.status.value) or self.n == 0:
            raise ValueError("Status of NumericalList object is not READY!")

    def set_status_ready(self):
        """Change status of input list."""
        self.status = Status.READY

    # ----------------------------------------------------------------
    # estimates of location
    # ----------------------------------------------------------------

    def arithmetic_mean(self):
        """Returns arithmetic mean [float]."""
        return np.mean(self.data)

    def weighted_arithmetic_mean(self, weights: list[float]):
        """Returns weighted (element-wise) arithmetic mean [float]."""
        return sum(np.multiply(self.data, weights))/sum(weights)

    def trimmed_mean(self, p:int):
        """Returns trimmed arithmetic mean [float] with the smallest and 
        largest p elements skipped."""
        trimmed = sorted(self.data)[p:-p]
        return np.mean(trimmed)

    def geometric_mean(self):
        """Returns geometric mean [float]."""
        return statistics.geometric_mean(self.data)

    def exponential_mean(self, m: float):
        """Returns exponential mean [float] using exponent m."""
        return (sum([x**m for x in self.data])/self.n)**(1/m)

    def harmonic_mean(self):
        """Returns harmonic mean [float]."""
        return statistics.harmonic_mean(self.data)

    def median(self):
        """Returns median [float]."""
        return statistics.median(self.data)

    def weighted_median(self, weights: list[float]):
        """Returns (element-wise) weighted median [float]."""
        weighted_list = []
        for i in range(self.n):
            weighted_list.extend([self.data[i]]*weights[i])
        return statistics.median(weighted_list)

    def percentile(self, per: int):
        """Return percentile value [float]."""
        sort = sorted(self.data)
        # return np.percentile(self.data, per)
        return sort[int(per/100*len(sort))]

    # ----------------------------------------------------------------
    # estimates of variability
    # ----------------------------------------------------------------

    def mu(self, k: int):
        """Returns the k-th statistical moment [float] related to the 
        arithmetic mean."""
        mean = self.arithmetic_mean()
        return np.mean([(i-mean)**k for i in self.data])

    def avg_absolute_deviation_from_mean(self):
        """Returns the mean deviation from the mean [float]."""
        mean = self.arithmetic_mean()
        return np.mean([abs(i-mean) for i in self.data])

    def avg_absolute_deviation_from_median(self):
        """Returns the mean deviation from the median [float]."""
        median = self.median()
        return np.mean([abs(i-median) for i in self.data])

    def median_absolute_deviaton(self):
        """Returns the median absolute deivation (MAD) [float]."""
        median = self.median()
        deviations = [abs(i-median) for i in self.data]
        return statistics.median(deviations)
        
    def variance(self, biased: bool):
        """Returns the (biased/ unbiased) variance [float]"""
        mu2 = self.mu(k=2)
        if biased:
            return mu2
        else:
            return mu2 * self.n/(self.n-1)

    def stdev(self, biased: bool):
        """Returns the (biased/ unbiased) standard deviation from 
        arithmetic mean [float]."""
        mu2 = self.mu(k=2)
        n = self.n
        if biased:
            return mu2**(1/2)
        else:
            return (mu2*n/(n-1))**(1/2)

    def range(self):
        """Returns range [float]."""
        return max(self.data)-min(self.data)

    def iqr(self):
        """Returns IQR [float]."""
        sort = sorted(self.data)
        index_25 = int(0.25*len(sort))
        index_75 = int(0.75*len(sort))
        # return np.subtract(*np.percentile(self.data, [75, 25]))
        return sort[index_75] - sort[index_25]

    # ----------------------------------------------------------------
    # estimates of distribution
    # ----------------------------------------------------------------

    def coefficient_of_skewness(self, biased: bool):
        """Returns (biased/ unbiased) skewness [float]."""
        stdev = self.stdev(biased=True)
        mu3 = self.mu(k=3)
        skew = mu3/stdev**3
        if biased:
            return skew
        else:
            return skew*(self.n**2)/((self.n-1)*(self.n-2))

    def coefficient_of_kurtosis(self, biased:bool):
        """Returns (biased/ unbiased) kortosis [float]."""
        stdev = self.stdev(biased=True)
        mu4 = self.mu(k=4)
        kurt = mu4/stdev**4
        if biased:
            return kurt
        else:
            return kurt*(self.n**3)/((self.n-1)*(self.n-2)*(self.n-3))
    
    def mode(self):
        """Returns mode [float]."""
        c = Counter(self.data)
        return [k for k, v in c.items() if v == c.most_common(1)[0][1]]
