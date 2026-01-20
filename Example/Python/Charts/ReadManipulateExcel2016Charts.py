import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_read_manipulate_excel2016_charts():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleReadManipulateExcel2016Charts.xlsx")
    workbook = cells.Workbook(input_file)

    worksheet = workbook.worksheets[0]

    for i in range(len(worksheet.charts)):
        chart = worksheet.charts[i]
        print(chart.type)
        chart.title.text = f"Chart Type is {chart.type}"

    output_file = os.path.join(output_dir, "outputReadManipulateExcel2016Charts.xlsx")
    workbook.save(output_file)

    print("ReadManipulateExcel2016Charts executed successfully.")

if __name__ == "__main__":
    run_read_manipulate_excel2016_charts()
