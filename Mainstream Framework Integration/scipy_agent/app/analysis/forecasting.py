import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing


class ForecastingAnalysis:

    @staticmethod
    def forecast(values, steps=5):

        arr = np.array(values, dtype=float)

        model = ExponentialSmoothing(arr)
        fit = model.fit()

        forecast = fit.forecast(steps)

        return forecast.tolist()