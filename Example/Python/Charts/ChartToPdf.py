import os
import io
from aspose.cells import Workbook
from aspose.cells.charts import Chart

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_chart_to_pdf():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load excel file containing charts
    workbook = Workbook(os.path.join(source_dir, "sampleChartToPdf.xlsx"))

    # Access first worksheet
    worksheet = workbook.worksheets[0]

    # Access first chart inside the worksheet
    chart = worksheet.charts[0]

    # Save the chart into pdf format
    chart.to_pdf(os.path.join(output_dir, "outputChartToPdf.pdf"))

    # Save the chart into pdf format in stream
    stream = io.BytesIO()
    chart.to_pdf(stream)

    print("ChartToPdf executed successfully.")

if __name__ == "__main__":
    run_chart_to_pdf()