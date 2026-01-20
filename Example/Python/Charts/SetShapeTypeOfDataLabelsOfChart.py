import os
import aspose.cells as cells
from aspose.cells.drawing import DataLabelShapeType

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_set_shape_type_of_data_labels_of_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "sampleSetShapeTypeOfDataLabelsOfChart.xlsx")
    workbook = cells.Workbook(workbook_path)

    worksheet = workbook.worksheets[0]
    chart = worksheet.charts[0]
    series = chart.n_series[0]

    series.data_labels.shape_type = DataLabelShapeType.WEDGE_ELLIPSE_CALLOUT

    output_path = os.path.join(output_dir, "outputSetShapeTypeOfDataLabelsOfChart.xlsx")
    workbook.save(output_path)

    print("SetShapeTypeOfDataLabelsOfChart executed successfully.")

if __name__ == "__main__":
    run_set_shape_type_of_data_labels_of_chart()
