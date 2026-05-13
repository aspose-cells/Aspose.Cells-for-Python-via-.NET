from app.analysis.fft_analysis import FFTAnalysis

def test_fft():

    values = [1, 2, 3, 4, 5]

    result = FFTAnalysis.analyze(values)

    assert len(result) > 0