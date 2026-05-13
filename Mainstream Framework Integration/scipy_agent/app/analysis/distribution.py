import numpy as np
from scipy.stats import normaltest


class DistributionAnalysis:

    @staticmethod
    def check_normal_distribution(values):

        arr = np.array(values, dtype=float)

        stat, p = normaltest(arr)

        return {
            "statistic": float(stat),
            "pvalue": float(p),
            "is_normal": p > 0.05
        }