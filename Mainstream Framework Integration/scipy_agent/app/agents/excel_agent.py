from excel.reader import ExcelReader
from excel.writer import ExcelWriter
from excel.detector import ColumnDetector

from tools.anomaly_tool import AnomalyTool
from tools.regression_tool import RegressionTool
from tools.trend_tool import TrendTool
from tools.fft_tool import FFTTool

from llm.planner import Planner


class ExcelAnalysisAgent:

    def __init__(self):
        self.reader = ExcelReader()
        self.writer = ExcelWriter()
        self.detector = ColumnDetector()

        self.planner = Planner()

        self.anomaly_tool = AnomalyTool()
        self.regression_tool = RegressionTool()
        self.trend_tool = TrendTool()
        self.fft_tool = FFTTool()

    def run(self, input_file, output_file, user_prompt):
        workbook = self.reader.load_workbook(input_file)

        sheet = self.reader.get_first_sheet(workbook)

        numeric_columns = self.detector.detect_numeric_columns(sheet)

        selected_tools = self.planner.plan(user_prompt)

        summary_lines = []

        if "anomaly_detection" in selected_tools:
            for col in numeric_columns:
                anomalies = self.anomaly_tool.run(sheet, col)

                summary_lines.append(
                    f"Column {col}: {len(anomalies)} anomalies"
                )

        if "trend_analysis" in selected_tools:
            for col in numeric_columns:
                trend = self.trend_tool.run(sheet, col)

                summary_lines.append(
                    f"Column {col}: trend calculated ({len(trend)} points)"
                )

        if "fft_analysis" in selected_tools:
            for col in numeric_columns:
                fft_result = self.fft_tool.run(sheet, col)

                summary_lines.append(
                    f"Column {col}: fft calculated ({len(fft_result)} values)"
                )

        if "regression_analysis" in selected_tools:
            if len(numeric_columns) >= 2:
                result = self.regression_tool.run(
                    sheet,
                    numeric_columns[0],
                    numeric_columns[1]
                )

                summary_lines.append(
                    f"Regression slope={result['slope']:.2f}, intercept={result['intercept']:.2f}"
                )

        summary_text = "\n".join(summary_lines)

        self.writer.add_summary_sheet(workbook, summary_text)

        self.writer.save(workbook, output_file)
        