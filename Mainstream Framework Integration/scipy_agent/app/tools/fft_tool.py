from analysis.fft_analysis import FFTAnalyzer


class FFTTool:

    def run(self, sheet, column_index):
        analyzer = FFTAnalyzer()

        values = []

        max_row = sheet.cells.max_data_row

        for row in range(1, max_row + 1):
            value = sheet.cells.get(row, column_index).value

            if isinstance(value, (int, float)):
                values.append(value)

        return analyzer.analyze(values)