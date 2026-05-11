import numpy as np


class TrendAnalyzer:

    def moving_average(self, values, window=3):
        return np.convolve(values, np.ones(window), 'valid') / window