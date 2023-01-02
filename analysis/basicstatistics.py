
import numpy as np
from collections import Counter

class BasicStatistics:
    
    def __init__(self, input):
        """Constructor for input list.

        Args:
            input (list): input data 
        """
        self.input = input
        
    def mean_arithmetic(self):
        """Returns the arithmetic mean of an input list of float numbers.

        Returns:
            float: arithmetic mean
        """
        return sum(self.input)/len(self.input)

    def mean_geometric(self):
        """Returns the geometric mean of an input list of float numbers.

        Returns:
            float: geometric mean
        """
        return (np.prod(self.input))**(1/len(self.input))

    def mean_exponential(self, m):
        """Returns the exponential mean of an input list of float numbers.

        Returns:
            float: exponential mean
        """
        n = len(self.input)
        input_modified = [x**m for x in self.input]
        mean = (sum(input_modified)/n)**(1/m)
        return mean

    def mean_harmonic(self):
        """Returns the harmonic mean of an input list of float numbers.

        Returns:
            float: harmonic mean
        """
        n = len(self.input)
        input_modified = [1/x for x in self.input]
        mean = n/(sum(input_modified))
        return mean

    def mean_median(self):
        """Returns the median of an input list of float numbers.
        If the length of the input list is even, the arithmetic
        mean of the left and right median is returned.

        Returns:
            float: median
        """
        n = len(self.input)
        input_sorted = sorted(self.input)
        
        # gerade 
        if n%2 == 0:
            index_1 = int(n/2)
            index_2 = int(n/2+1)
            return (input_sorted[index_1-1] + input_sorted[index_2-1])/2
        
        # ungerade
        else: 
            index = int((n+1)/2)
            return input_sorted[index-1]

    def mode(self):
        """Returns a list with a single or multiple modes of an 
        input list of float numbers. 

        Returns:
            list: mode(s)
        """
        c = Counter(self.input)
        mode_list = [k for k, v in c.items() if v == c.most_common(1)[0][1]]
        return mode_list
