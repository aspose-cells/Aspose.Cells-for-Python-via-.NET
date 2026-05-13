from analysis.anomaly import AnomalyAnalysis


def run_anomaly(values):
    return AnomalyAnalysis.detect_zscore(values)