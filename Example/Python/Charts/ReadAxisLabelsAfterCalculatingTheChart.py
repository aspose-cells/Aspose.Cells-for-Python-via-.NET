import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_read_axis_labels_after_calculating_the_chart():
    source_dir = get_source_directory()
    workbook = cells.Workbook(os.path.join(source_dir, "sampleReadAxisLabelsAfterCalculatingTheChart.xlsx"))
    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    chart.calculate()

    lst_labels = chart.category_axis.axis_labels

    print("Category Axis Labels:")
    print("---------------------")
    for label in lst_labels:
        print(label)

    print("ReadAxisLabelsAfterCalculatingTheChart executed successfully.")

if __name__ == "__main__":
    run_read_axis_labels_after_calculating_the_chart()