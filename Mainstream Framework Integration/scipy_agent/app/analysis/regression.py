import numpy as np
from scipy.stats import linregress


class RegressionAnalysis:

    @staticmethod
    def linear_regression(values):

        x = np.arange(len(values))
        y = np.array(values, dtype=float)

        result = linregress(x, y)

        return {
            "slope": result.slope,
            "intercept": result.intercept,
            "rvalue": result.rvalue,
            "pvalue": result.pvalue,
            "stderr": result.stderr
        }