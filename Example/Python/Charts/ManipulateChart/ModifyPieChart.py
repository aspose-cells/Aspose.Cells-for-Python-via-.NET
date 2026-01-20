import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_modify_pie_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = cells.Workbook(os.path.join(source_dir, "sampleModifyPieChart.xlsx"))
    sheet = workbook.worksheets[1]
    chart = sheet.charts[0]

    data_labels = chart.n_series[0].points[2].data_labels
    data_labels.text = "Unided Kingdom, 400K "

    workbook.save(os.path.join(output_dir, "outputModifyPieChart.xlsx"))

    print("ModifyPieChart executed successfully.")

if __name__ == "__main__":
    run_modify_pie_chart()