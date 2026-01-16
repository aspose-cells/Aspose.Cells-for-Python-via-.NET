import os
from aspose.cells import Workbook
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_change_chart_size_and_position():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "sampleChangeChartSizeAndPosition.xlsx")
    workbook = Workbook(input_path)

    worksheet = workbook.worksheets[0]

    chart = worksheet.charts[0]

    chart.chart_object.width = 400
    chart.chart_object.height = 300
    chart.chart_object.x = 250
    chart.chart_object.y = 150

    output_path = os.path.join(output_dir, "outputChangeChartSizeAndPosition.xlsx")
    workbook.save(output_path)

    print("ChangeChartSizeAndPosition executed successfully.")

if __name__ == "__main__":
    run_change_chart_size_and_position()