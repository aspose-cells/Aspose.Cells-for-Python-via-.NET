from analysis.anomaly import AnomalyAnalyzer
from excel.formatter import Formatter


class AnomalyTool:

    def run(self, sheet, column_index):
        analyzer = AnomalyAnalyzer()
        formatter = Formatter()

        values = []

        max_row = sheet.cells.max_data_row

        for row in range(1, max_row + 1):
            value = sheet.cells.get(row, column_index).value

            if isinstance(value, (int, float)):
                values.append(value)
            else:
                values.append(0)

        anomalies = analyzer.detect(values)

        for anomaly_index in anomalies:
            formatter.highlight_cell_red(
                sheet,
                anomaly_index + 1,
                column_index
            )

        return anomalies