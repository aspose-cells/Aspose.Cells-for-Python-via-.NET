import os
import aspose.cells as cells
from aspose.pydrawing import Color
from aspose.cells.drawing import GradientStyleType

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_setting_titles_axes():
    output_dir = get_output_directory()

    # Create a new workbook and get the first worksheet
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Fill sample data
    worksheet.cells.get("A1").put_value(50)
    worksheet.cells.get("A2").put_value(100)
    worksheet.cells.get("A3").put_value(150)
    worksheet.cells.get("B1").put_value(60)
    worksheet.cells.get("B2").put_value(32)
    worksheet.cells.get("B3").put_value(50)

    # Add a column chart
    chart_index = worksheet.charts.add(cells.charts.ChartType.COLUMN, 5, 0, 25, 10)
    chart = worksheet.charts[chart_index]

    # Set chart data source
    chart.n_series.add("A1:B3", True)

    # Format areas
    chart.plot_area.area.foreground_color = Color.blue
    chart.chart_area.area.foreground_color = Color.yellow
    chart.n_series[0].area.foreground_color = Color.red
    chart.n_series[0].points[0].area.foreground_color = Color.cyan

    # Gradient fill for the second series
    chart.n_series[1].area.fill_format.set_one_color_gradient(
        Color.lime, 1.0, GradientStyleType.HORIZONTAL, 1
    )

    # Set titles and formatting
    chart.title.text = "Title"
    chart.title.font.color = Color.blue
    chart.category_axis.title.text = "Category"
    chart.value_axis.title.text = "Value"

    # Save the workbook
    output_path = os.path.join(output_dir, "outputSettingTitlesAxes.xlsx")
    workbook.save(output_path)

    print("SettingTitlesAxes executed successfully.")

if __name__ == "__main__":
    run_setting_titles_axes()
