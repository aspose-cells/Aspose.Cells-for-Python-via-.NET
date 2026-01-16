import os
from aspose.cells import *
from aspose.cells.drawing import *
from aspose.cells.charts import *

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_change_tick_label_direction():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "SampleChangeTickLabelDirection.xlsx")
    workbook = Workbook(input_path)

    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]

    chart.category_axis.tick_labels.direction_type = ChartTextDirectionType.HORIZONTAL

    output_path = os.path.join(output_dir, "outputChangeChartDataLableDirection.xlsx")
    workbook.save(output_path)

    print("ChangeTickLabelDirection executed successfully.")

if __name__ == "__main__":
    run_change_tick_label_direction()