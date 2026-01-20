import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_create_chart_pdf_with_desired_page_size():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleCreateChartPDFWithDesiredPageSize.xlsx")
    workbook = cells.Workbook(input_file)

    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    output_file = os.path.join(output_dir, "outputCreateChartPDFWithDesiredPageSize.pdf")
    chart.to_pdf(output_file, 7.0, 7.0, cells.PageLayoutAlignmentType.CENTER, cells.PageLayoutAlignmentType.CENTER)

    print("CreateChartPDFWithDesiredPageSize executed successfully.")

if __name__ == "__main__":
    run_create_chart_pdf_with_desired_page_size()
