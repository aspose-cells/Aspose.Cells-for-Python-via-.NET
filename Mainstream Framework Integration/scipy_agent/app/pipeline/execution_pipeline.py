# app/pipeline/execution_pipeline.py

from excel.reader import ExcelReader
from registry.tool_registry import TOOL_REGISTRY
from aspose.cells import Workbook, Style,BackgroundType
from aspose.pydrawing import Color
import pandas as pd
from renderer.chart_renderer import ChartRenderer

class ExecutionPipeline:

    def execute(self, file_path, plan):

        # -------------------------
        # 1. Load dataframe
        # -------------------------
        df = ExcelReader.load_sheet_as_dataframe(file_path)



        # -------------------------
        # 2. Auto profiling
        # -------------------------
        numeric_df = df.select_dtypes(include=['number'])

        numeric_columns = numeric_df.columns.tolist()

        results = {}

        # -------------------------
        # 3. Execute tools
        # -------------------------
        tools = plan.get("tools", [])

        if not isinstance(tools, list):
            tools = [tools]

        for tool_name in tools:

            print(f"Running tool: {tool_name}")

            tool_entry = TOOL_REGISTRY.get(tool_name)

            tool_func = tool_entry["func"]
            tool_input_type = tool_entry["input"]

            if not tool_func:
                print(f"Tool not found: {tool_name}")
                continue

            try:

                # =====================================
                # Column-based tools
                # =====================================
                if tool_name in [
                    "anomaly",
                    "trend",
                    "forecast",
                    "fft",
                    "regression",
                    "statistics",
                    "seasonality",
                    "outlier",
                    "distribution",
                    "smoothing",
                    "change_point"
                ]:

                    tool_results = {}

                    for col in numeric_columns:

                        values = (
                            numeric_df[col]
                            .dropna()
                            .astype(float)
                            .tolist()
                        )

                        if len(values) < 3:
                            continue

                        tool_results[col] = tool_func(values)

                    results[tool_name] = tool_results

                # =====================================
                # DataFrame-based tools
                # =====================================
                elif tool_name in [
                    "correlation",
                    "pca",
                    "clustering"
                ]:

                    results[tool_name] = tool_func(numeric_df)

                # =====================================
                # Unknown
                # =====================================
                else:

                    print(f"Unsupported tool mode: {tool_name}")

            except Exception as e:

                results[tool_name] = {
                    "error": str(e)
                }

        # -------------------------
        # 4. Metadata
        # -------------------------
        final_result = {
            "row_count": len(df),
            "column_count": len(df.columns),
            "numeric_columns": numeric_columns,
            "analysis_results": results
        }
        self.apply_highlights(file_path, results)

        return final_result



    def apply_highlights(self, file_path, results):

        # -------------------------
        # Load workbook
        # -------------------------
        wb = Workbook(file_path)

        # First worksheet
        ws = wb.worksheets[0]

        # -------------------------
        # Get anomaly results
        # -------------------------
        anomaly_results = results.get("anomaly", {})

        # -------------------------
        # Loop each column
        # -------------------------
        for column_name, anomalies in anomaly_results.items():

            # Skip empty
            if not anomalies:
                continue

            # -------------------------
            # Find column index
            # -------------------------
            cells = ws.cells

            max_col = cells.max_data_column

            excel_col = -1

            for c in range(max_col + 1):

                header_value = cells.get(0, c).string_value

                if header_value == column_name:
                    excel_col = c
                    break

            if excel_col == -1:
                continue

            # -------------------------
            # Highlight anomaly cells
            # -------------------------
            for item in anomalies:
                pandas_index = item["index"]

                # +2 because:
                # +1 => skip header
                # +1 => pandas starts at 0
                excel_row = pandas_index + 2

                cell = cells.get(excel_row - 1, excel_col)

                style = cell.get_style()

                # Red fill
                style.foreground_color = Color.red
                style.pattern = BackgroundType.SOLID


                # Optional: white font
                font = style.font
                font.color = Color.white
                font.is_bold = True

                cell.set_style(style)

        # -------------------------
        # Save workbook
        # -------------------------
        wb.save(file_path)