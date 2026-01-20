import os
import aspose.cells as cells
import aspose.cells.drawing as acd

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_adding_label_control_in_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "sampleAddingLabelControlInChart.xls")
    workbook = cells.Workbook(input_path)

    sheet = workbook.worksheets[0]
    chart = sheet.charts[0]

    label = chart.shapes.add_label_in_chart(600, 600, 350, 900)
    label.text = "A Label In Chart"
    label.placement = acd.PlacementType.FREE_FLOATING

    output_path = os.path.join(output_dir, "outputAddingLabelControlInChart.xls")
    workbook.save(output_path)

    print("AddingLabelControlInChart executed successfully.")

if __name__ == "__main__":
    run_adding_label_control_in_chart()