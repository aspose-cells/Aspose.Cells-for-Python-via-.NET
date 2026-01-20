import os
import aspose.cells as cells
from aspose.cells.drawing import MsoLineDashStyle
import io

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "01_SourceDirectory"))


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_adding_picture_in_chart():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the existing workbook
    workbook_path = os.path.join(source_dir, "sampleAddingPictureInChart.xls")
    workbook = cells.Workbook(workbook_path)

    # Path to the image to be added
    image_path = os.path.join(source_dir, "sampleAddingPictureInChart.png")

    # Access the first worksheet and its first chart
    sheet = workbook.worksheets[0]
    chart = sheet.charts[0]

    with open(image_path, 'rb') as file:
        input_stream = io.BytesIO(file.read())

    # Add a picture to the chart (using image file path overload)
    pic = chart.shapes.add_picture_in_chart(50, 50, input_stream, 200, 200)

    # Configure the picture's line format
    line_format = pic.line
    line_format.dash_style = MsoLineDashStyle.SOLID
    line_format.weight = 4.0

    # Save the modified workbook
    output_path = os.path.join(output_dir, "outputAddingPictureInChart.xls")
    workbook.save(output_path)

    print("AddingPictureInChart executed successfully.")


if __name__ == "__main__":
    run_adding_picture_in_chart()