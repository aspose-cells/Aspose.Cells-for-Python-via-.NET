"""
'''from tools.anomaly_tool import run_anomaly
from tools.regression_tool import run_regression
from tools.trend_tool import run_trend
from tools.fft_tool import run_fft
from tools.statistics_tool import run_statistics
from tools.forecast_tool import run_forecast


TOOL_REGISTRY = {
    "anomaly": run_anomaly,
    "regression": run_regression,
    "trend": run_trend,
    "fft": run_fft,
    "statistics": run_statistics,
    "forecast": run_forecast
}
"""
from tools.anomaly_tool import run_anomaly
from tools.trend_tool import run_trend
from tools.correlation_tool import run_correlation
from tools.pca_tool import run_pca

TOOL_REGISTRY = {
    "anomaly": {
        "func": run_anomaly,
        "input": "series"
    },

    "trend": {
        "func": run_trend,
        "input": "series"
    },

    "correlation": {
        "func": run_correlation,
        "input": "dataframe"
    },

    "pca": {
        "func": run_pca,
        "input": "dataframe"
    }
}