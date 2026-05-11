from analysis.regression import RegressionAnalyzer


class RegressionTool:

    def run(self, sheet, x_col, y_col):
        analyzer = RegressionAnalyzer()

        x_values = []
        y_values = []

        max_row = sheet.cells.max_data_row

        for row in range(1, max_row + 1):
            x = sheet.cells.get(row, x_col).value
            y = sheet.cells.get(row, y_col).value

            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                x_values.append(x)
                y_values.append(y)

        return analyzer.fit(x_values, y_values)