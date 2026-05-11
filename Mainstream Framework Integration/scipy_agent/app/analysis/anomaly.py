import numpy as np
from scipy.stats import zscore


class AnomalyAnalyzer:

    def detect(self, values, threshold=2.0):
        array = np.array(values, dtype=float)

        scores = zscore(array)

        anomalies = []

        for index, score in enumerate(scores):
            if abs(score) > threshold:
                anomalies.append(index)

        return anomalies