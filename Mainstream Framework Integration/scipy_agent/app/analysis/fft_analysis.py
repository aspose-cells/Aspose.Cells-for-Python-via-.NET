import numpy as np
from scipy.fft import fft


class FFTAnalysis:

    @staticmethod
    def analyze(values):

        arr = np.array(values, dtype=float)

        spectrum = fft(arr)

        magnitude = np.abs(spectrum)

        return magnitude.tolist()