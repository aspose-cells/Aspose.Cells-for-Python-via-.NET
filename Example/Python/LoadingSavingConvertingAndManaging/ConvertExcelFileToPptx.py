from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color
from datetime import datetime
import os
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def convert_excel_file_to_pptx():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = Workbook(os.path.join(source_dir, "Book1.xlsx"))
    workbook.save(os.path.join(output_dir, "Book1.pptx"), SaveFormat.PPTX)

    print("ConvertExcelFileToPptx executed successfully.")

if __name__ == "__main__":
    convert_excel_file_to_pptx()