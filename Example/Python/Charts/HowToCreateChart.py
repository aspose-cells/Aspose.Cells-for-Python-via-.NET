import os
from aspose.cells import *
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_how_to_create_chart():
    output_dir = get_output_directory()

    # Instantiating a Workbook object
    workbook = Workbook()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[0]

    # Adding sample values to cells
    worksheet.cells.get("A1").put_value(50.0)
    worksheet.cells.get("A2").put_value(100.0)
    worksheet.cells.get("A3").put_value(150.0)
    worksheet.cells.get("B1").put_value(4.0)
    worksheet.cells.get("B2").put_value(20.0)
    worksheet.cells.get("B3").put_value(50.0)

    # Adding a chart to the worksheet
    chart_index = worksheet.charts.add(ChartType.PYRAMID, 5, 0, 15, 5)

    # Accessing the instance of the newly added chart
    chart = worksheet.charts[chart_index]

    # Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.n_series.add("A1:B3", True)

    # Saving the Excel file
    output_file = os.path.join(output_dir, "outputHowToCreateChart.xlsx")
    workbook.save(output_file)

    print("HowToCreateChart executed successfully.")

if __name__ == "__main__":
    run_how_to_create_chart()