import os
import aspose.cells as cells
from aspose.cells import SaveFormat
from aspose.cells.charts import ChartType
from aspose.pydrawing import Color

# Attempt to import FormattingType from possible namespaces
try:
    from aspose.cells.drawing import FormattingType
except ImportError:
    from aspose.cells.charts import FormattingType


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_create_line_with_data_marker_chart():
    output_dir = get_output_directory()

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Set column titles
    worksheet.cells.get(0, 0).put_value("X")
    worksheet.cells.get(0, 1).put_value("Y")

    # First data range
    for i in range(1, 21):
        worksheet.cells.get(i, 0).put_value(i)
        worksheet.cells.get(i, 1).put_value(0.8)

    # Second data range
    for i in range(21, 41):
        worksheet.cells.get(i, 0).put_value(i - 20)
        worksheet.cells.get(i, 1).put_value(0.9)

    # Add LineWithDataMarkers chart
    idx = worksheet.charts.add(ChartType.LINE_WITH_DATA_MARKERS, 1, 3, 20, 20)
    chart = worksheet.charts[idx]

    chart.style = 3
    chart.auto_scaling = True
    chart.plot_area.area.foreground_color = Color.white
    chart.title.text = "Sample Chart"
    chart.type = ChartType.LINE_WITH_DATA_MARKERS
    chart.category_axis.title.text = "Units"

    # Add series
    s2_idx = chart.n_series.add("A2:A2", True)
    s3_idx = chart.n_series.add("A22:A22", True)

    chart.n_series.is_color_varied = True

    # Configure first series
    chart.n_series[s2_idx].area.formatting = FormattingType.CUSTOM
    chart.n_series[s2_idx].marker.area.foreground_color = Color.yellow
    chart.n_series[s2_idx].marker.border.is_visible = False
    chart.n_series[s2_idx].x_values = "A2:A21"
    chart.n_series[s2_idx].values = "B2:B21"

    # Configure second series
    chart.n_series[s3_idx].area.formatting = FormattingType.CUSTOM
    chart.n_series[s3_idx].marker.area.foreground_color = Color.green
    chart.n_series[s3_idx].marker.border.is_visible = False
    chart.n_series[s3_idx].x_values = "A22:A41"
    chart.n_series[s3_idx].values = "B22:B41"

    # Save workbook
    output_path = os.path.join(output_dir, "LineWithDataMarkerChart.xlsx")
    workbook.save(output_path, SaveFormat.XLSX)

    print("CreateLineWithDataMarkerChart executed successfully.")


if __name__ == "__main__":
    run_create_line_with_data_marker_chart()