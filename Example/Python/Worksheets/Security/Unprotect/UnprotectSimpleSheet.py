import os
from aspose import pydrawing
from aspose.cells import Workbook, SaveFormat
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Unprotect/UnprotectSimpleSheet"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    workbook = Workbook(str(data_dir / "book1.xls"))
    worksheet = workbook.worksheets[0]
    worksheet.unprotect()
    output_dir = get_output_directory()
    os.makedirs(str(output_dir), exist_ok=True)
    workbook.save(str(output_dir / "output.out.xls"), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    run()