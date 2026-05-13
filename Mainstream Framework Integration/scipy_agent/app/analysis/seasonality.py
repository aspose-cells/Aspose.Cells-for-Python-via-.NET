from statsmodels.tsa.seasonal import seasonal_decompose
import pandas as pd


class SeasonalityAnalysis:

    @staticmethod
    def analyze(values):

        series = pd.Series(values)

        result = seasonal_decompose(series, period=4, model='additive')

        return {
            "trend": result.trend.tolist(),
            "seasonal": result.seasonal.tolist(),
            "residual": result.resid.tolist()
        }