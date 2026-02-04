import os
from pathlib import Path
import aspose.cells as cells

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run_specify_far_east_and_latin_name_of_font_in_text_options_of_shape():
    # Create empty workbook.
    workbook = cells.Workbook()

    # Access first worksheet.
    worksheet = workbook.worksheets[0]

    # Add textbox inside the worksheet.
    idx = worksheet.text_boxes.add(5, 5, 50, 200)
    textbox = worksheet.text_boxes[idx]

    # Set the text of the textbox.
    textbox.text = "こんにちは世界"

    # Specify the Far East and Latin name of the font.
    textbox.text_options.latin_name = "Comic Sans MS"
    textbox.text_options.far_east_name = "KaiTi"

    # Save the output Excel file.
    output_dir = get_output_directory()
    output_path = os.path.join(output_dir, "outputSpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape.xlsx")
    workbook.save(output_path, cells.SaveFormat.XLSX)

    print("SpecifyFarEastAndLatinNameOfFontInTextOptionsOfShape executed successfully.")

if __name__ == "__main__":
    run_specify_far_east_and_latin_name_of_font_in_text_options_of_shape()