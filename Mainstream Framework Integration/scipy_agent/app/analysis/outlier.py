import numpy as np

class OutlierAnalysis:

    @staticmethod
    def iqr_outliers(values):

        arr = np.array(values, dtype=float)

        q1 = np.percentile(arr, 25)
        q3 = np.percentile(arr, 75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        result = []

        for i, v in enumerate(arr):
            if v < lower or v > upper:
                result.append({
                    "index": i,
                    "value": float(v)
                })

        return result