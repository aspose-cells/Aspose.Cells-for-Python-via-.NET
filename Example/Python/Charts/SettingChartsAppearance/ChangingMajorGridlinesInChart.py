import os
import aspose.cells as cells
from aspose.pydrawing import Color
from aspose.cells.charts import ChartType
from aspose.cells.drawing import GradientStyleType


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_changing_major_gridlines_in_chart():
    # Instantiating a Workbook object
    workbook = cells.Workbook()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[0]

    # Adding sample values to cells
    worksheet.cells.get("A1").put_value(50)
    worksheet.cells.get("A2").put_value(100)
    worksheet.cells.get("A3").put_value(150)
    worksheet.cells.get("B1").put_value(60)
    worksheet.cells.get("B2").put_value(32)
    worksheet.cells.get("B3").put_value(50)

    # Adding a chart to the worksheet
    chart_index = worksheet.charts.add(ChartType.COLUMN, 5, 0, 25, 10)

    # Accessing the instance of the newly added chart
    chart = worksheet.charts[chart_index]

    # Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.n_series.add("A1:B3", True)

    # Setting the foreground color of the plot area
    chart.plot_area.area.foreground_color = Color.blue

    # Setting the foreground color of the chart area
    chart.chart_area.area.foreground_color = Color.yellow

    # Setting the foreground color of the 1st SeriesCollection area
    chart.n_series[0].area.foreground_color = Color.red

    # Setting the foreground color of the area of the 1st SeriesCollection point
    chart.n_series[0].points[0].area.foreground_color = Color.cyan

    # Filling the area of the 2nd SeriesCollection with a gradient
    chart.n_series[1].area.fill_format.set_one_color_gradient(
        Color.lime, 1.0, GradientStyleType.HORIZONTAL, 1
    )

    # Setting the color of Category Axis' major gridlines to silver
    chart.category_axis.major_grid_lines.color = Color.silver

    # Setting the color of Value Axis' major gridlines to red
    chart.value_axis.major_grid_lines.color = Color.red

    # Saving the Excel file
    output_path = os.path.join(get_output_directory(), "outputChangingMajorGridlinesInChart.xlsx")
    workbook.save(output_path)

    print("ChangingMajorGridlinesInChart executed successfully.")


if __name__ == "__main__":
    run_changing_major_gridlines_in_chart()
