import os
import aspose.cells as cells
from aspose.cells.charts import ChartType, ChartMarkerType
from aspose.cells.drawing import GradientStyleType, LineType, WeightType
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_setting_chart_lines():
    # Instantiate a Workbook object
    workbook = cells.Workbook()

    # Obtain the reference of the first worksheet
    worksheet = workbook.worksheets[0]

    # Add sample values to cells
    worksheet.cells.get("A1").put_value(50)
    worksheet.cells.get("A2").put_value(100)
    worksheet.cells.get("A3").put_value(150)
    worksheet.cells.get("B1").put_value(60)
    worksheet.cells.get("B2").put_value(32)
    worksheet.cells.get("B3").put_value(50)

    # Add a column chart to the worksheet
    chart_index = worksheet.charts.add(ChartType.COLUMN, 5, 0, 25, 10)
    chart = worksheet.charts[chart_index]

    # Set the chart data source
    chart.n_series.add("A1:B3", True)

    # Set foreground colors
    chart.plot_area.area.foreground_color = Color.get_blue()
    chart.chart_area.area.foreground_color = Color.get_yellow()
    chart.n_series[0].area.foreground_color = Color.get_red()
    chart.n_series[0].points[0].area.foreground_color = Color.get_cyan()

    # Fill the second series area with a horizontal gradient
    chart.n_series[1].area.fill_format.set_one_color_gradient(
        Color.get_lime(), 1, GradientStyleType.HORIZONTAL, 1
    )

    # Apply a dotted line style to the first series
    chart.n_series[0].border.style = LineType.DOT

    # Set a triangular marker for the first series
    chart.n_series[0].marker.marker_style = ChartMarkerType.TRIANGLE

    # Set medium line weight for the second series
    chart.n_series[1].border.weight = WeightType.MEDIUM_LINE

    # Save the workbook
    output_path = os.path.join(get_output_directory(), "outputSettingChartLines.xlsx")
    workbook.save(output_path)


if __name__ == "__main__":
    run_setting_chart_lines()
