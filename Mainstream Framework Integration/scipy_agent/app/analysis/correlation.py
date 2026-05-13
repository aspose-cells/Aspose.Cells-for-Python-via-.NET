import pandas as pd


class CorrelationAnalysis:

    @staticmethod
    def correlation_matrix(df):

        numeric_df = df.select_dtypes(include=['number'])

        return numeric_df.corr().to_dict()