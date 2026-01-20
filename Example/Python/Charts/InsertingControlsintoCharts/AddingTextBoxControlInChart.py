import os
import aspose.cells as cells
from aspose.cells.drawing import MsoLineDashStyle
from aspose.pydrawing import Color


def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "01_SourceDirectory"))


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_adding_text_box_control_in_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Open the existing file.
    input_path = os.path.join(source_dir, "sampleAddingTextBoxControlInChart.xls")
    workbook = cells.Workbook(input_path)

    # Get the chart in the first worksheet.
    sheet = workbook.worksheets[0]
    chart = sheet.charts[0]

    # Add a new textbox to the chart.
    textbox0 = chart.shapes.add_text_box_in_chart(400, 1100, 350, 2550)

    # Set the textbox text.
    textbox0.text = "Sales By Region"

    # Set font properties.
    textbox0.font.color = Color.maroon
    textbox0.font.is_bold = True
    textbox0.font.size = 14
    textbox0.font.is_italic = True

    # Configure line format.
    lineformat = textbox0.line
    lineformat.weight = 2.0
    lineformat.dash_style = MsoLineDashStyle.SOLID

    # Save the workbook.
    output_path = os.path.join(output_dir, "outputAddingTextBoxControlInChart.xls")
    workbook.save(output_path)

    print("AddingTextBoxControlInChart executed successfully.")


if __name__ == "__main__":
    run_adding_text_box_control_in_chart()
