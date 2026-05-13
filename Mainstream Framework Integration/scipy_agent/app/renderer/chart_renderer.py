from aspose.cells.charts import ChartType


class ChartRenderer:

    @staticmethod
    def add_line_chart(ws, row_count):

        chart_index = ws.charts.add(
            ChartType.LINE,
            5,
            5,
            25,
            15
        )

        chart = ws.charts[chart_index]

        chart.n_series.add(
            f"B2:B{row_count}",
            True
        )

        chart.n_series.category_data = f"A2:A{row_count}"

        chart.title.text = "Sales Trend"