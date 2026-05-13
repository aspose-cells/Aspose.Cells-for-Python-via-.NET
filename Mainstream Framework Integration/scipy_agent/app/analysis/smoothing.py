import pandas as pd


class SmoothingAnalysis:

    @staticmethod
    def moving_average(values, window=3):

        series = pd.Series(values)

        return series.rolling(window=window).mean().tolist()