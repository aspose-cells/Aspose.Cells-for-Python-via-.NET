from app.analysis.regression import RegressionAnalysis


def test_regression():

    values = [1, 2, 3, 4, 5]

    result = RegressionAnalysis.linear_regression(values)

    assert result["slope"] > 0
    