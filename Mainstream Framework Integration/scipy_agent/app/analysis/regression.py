import numpy as np
from scipy.optimize import curve_fit


class RegressionAnalyzer:

    def linear_func(self, x, a, b):
        return a * x + b

    def fit(self, x_values, y_values):
        x = np.array(x_values, dtype=float)
        y = np.array(y_values, dtype=float)

        params, _ = curve_fit(self.linear_func, x, y)

        return {
            "slope": params[0],
            "intercept": params[1]
        }