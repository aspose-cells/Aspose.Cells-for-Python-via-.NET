import numpy as np


class ChangePointAnalysis:

    @staticmethod
    def detect(values):

        arr = np.array(values, dtype=float)

        diffs = np.diff(arr)

        threshold = np.std(diffs) * 2

        result = []

        for i, d in enumerate(diffs):
            if abs(d) > threshold:
                result.append({
                    "position": i,
                    "change": float(d)
                })

        return result