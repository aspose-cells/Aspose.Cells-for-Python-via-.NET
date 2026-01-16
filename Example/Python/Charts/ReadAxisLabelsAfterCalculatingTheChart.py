import os
from aspose.cells import *
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_source_directory():
    return os.path.abspath(os.path.join(".",   "..", "..", "Data", "01_SourceDirectory"))

def run_read_axis_labels_after_calculating_the_chart():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleReadAxisLabelsAfterCalculatingTheChart.xlsx")
    workbook = Workbook(input_file)

    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    chart.calculate()

    lst_labels = chart.category_axis.axis_labels

    print("Category Axis Labels: ")
    print("---------------------")
    for label in lst_labels:
        print(label)

    print("ReadAxisLabelsAfterCalculatingTheChart executed successfully.")

if __name__ == "__main__":
    run_read_axis_labels_after_calculating_the_chart()