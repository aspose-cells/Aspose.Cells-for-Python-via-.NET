import numpy as np
from scipy.fft import fft


class FFTAnalyzer:

    def analyze(self, values):
        signal = np.array(values, dtype=float)

        result = fft(signal)

        magnitude = np.abs(result)

        return magnitude.tolist()