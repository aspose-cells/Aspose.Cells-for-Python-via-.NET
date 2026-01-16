import os
from aspose.cells import *
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_handle_automatic_units_of_chart_axis_like_microsoft_excel():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx")
    workbook = Workbook(input_file)

    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    output_file = os.path.join(output_dir, "outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf")
    chart.to_pdf(output_file)

    print("HandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel executed successfully.")

if __name__ == "__main__":
    run_handle_automatic_units_of_chart_axis_like_microsoft_excel()