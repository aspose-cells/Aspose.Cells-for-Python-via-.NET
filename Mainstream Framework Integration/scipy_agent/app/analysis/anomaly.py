import numpy as np
from scipy import stats


class AnomalyAnalysis:

    @staticmethod
    def detect_zscore(values, threshold=3):

        arr = np.array(values, dtype=float)

        z_scores = np.abs(stats.zscore(arr))

        anomalies = []

        for i, z in enumerate(z_scores):
            if z > threshold:
                anomalies.append({
                    "index": i,
                    "value": arr[i],
                    "zscore": float(z)
                })

        return anomalies