import os
from aspose.cells import Workbook, PageLayoutAlignmentType
from aspose.cells.charts import Chart

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_create_chart_pdf_with_desired_page_size():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load sample Excel file containing the chart.
    input_file = os.path.join(source_dir, "sampleCreateChartPDFWithDesiredPageSize.xlsx")
    workbook = Workbook(input_file)

    # Access first worksheet.
    worksheet = workbook.worksheets[0]

    # Access first chart inside the worksheet.
    chart = worksheet.charts[0]  # type: Chart

    # Create chart PDF with desired page size.
    output_file = os.path.join(output_dir, "outputCreateChartPDFWithDesiredPageSize.pdf")
    chart.to_pdf(output_file, 7.0, 7.0,
                 PageLayoutAlignmentType.CENTER,
                 PageLayoutAlignmentType.CENTER)

    print("CreateChartPDFWithDesiredPageSize executed successfully.")

if __name__ == "__main__":
    run_create_chart_pdf_with_desired_page_size()