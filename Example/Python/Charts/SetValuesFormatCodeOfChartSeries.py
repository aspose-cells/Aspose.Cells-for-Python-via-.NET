import os
from aspose.cells import Workbook
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_set_values_format_code_of_chart_series():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleSeries_ValuesFormatCode.xlsx")
    workbook = Workbook(input_file)

    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    chart.n_series.add("{10000, 20000, 30000, 40000}", True)

    series = chart.n_series[0]
    series.values_format_code = "$#,##0"

    output_file = os.path.join(output_dir, "outputSeries_ValuesFormatCode.xlsx")
    workbook.save(output_file)

    print("SetValuesFormatCodeOfChartSeries executed successfully.")

if __name__ == "__main__":
    run_set_values_format_code_of_chart_series()