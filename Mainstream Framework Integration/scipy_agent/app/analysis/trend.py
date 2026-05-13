import numpy as np
from scipy.signal import savgol_filter


class TrendAnalysis:

    @staticmethod
    def smooth(values):

        arr = np.array(values, dtype=float)

        if len(arr) < 5:
            return arr.tolist()

        smoothed = savgol_filter(arr, 5, 2)

        return smoothed.tolist()