import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_change_chart_size_and_position():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "sampleChangeChartSizeAndPosition.xlsx")
    workbook = cells.Workbook(workbook_path)

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
