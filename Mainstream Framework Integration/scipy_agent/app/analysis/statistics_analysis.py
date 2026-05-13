import numpy as np
from scipy.stats import skew, kurtosis


class StatisticsAnalysis:

    @staticmethod
    def describe(values):

        arr = np.array(values, dtype=float)

        return {
            "mean": float(np.mean(arr)),
            "median": float(np.median(arr)),
            "std": float(np.std(arr)),
            "variance": float(np.var(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "skewness": float(skew(arr)),
            "kurtosis": float(kurtosis(arr))
        }