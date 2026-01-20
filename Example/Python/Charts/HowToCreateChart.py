import os
import aspose.cells as cells
from aspose.cells.charts import ChartType


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_how_to_create_chart():
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    worksheet.cells.get("A1").put_value(50.0)
    worksheet.cells.get("A2").put_value(100.0)
    worksheet.cells.get("A3").put_value(150.0)
    worksheet.cells.get("B1").put_value(4.0)
    worksheet.cells.get("B2").put_value(20.0)
    worksheet.cells.get("B3").put_value(50.0)

    try:
        chart_type = ChartType.PYRAMID
    except AttributeError:
        chart_type = ChartType.PYRAMID3D

    chart_index = worksheet.charts.add(chart_type, 5, 0, 15, 5)

    chart = worksheet.charts[chart_index]
    chart.n_series.add("A1:B3", True)

    output_file = os.path.join(get_output_directory(), "outputHowToCreateChart.xlsx")
    workbook.save(output_file)

    print("HowToCreateChart executed successfully.")


if __name__ == "__main__":
    run_how_to_create_chart()
