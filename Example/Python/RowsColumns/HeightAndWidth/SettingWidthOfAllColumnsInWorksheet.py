import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/HeightAndWidth/SettingWidthOfAllColumnsInWorksheet"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    data_dir = Path(data_dir)
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True, exist_ok=True)

    # Opening the Excel file
    workbook = Workbook(str(data_dir / "book1.xls"))

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]

    # Setting the width of all columns in the worksheet to 20.5
    worksheet.cells.standard_width = 20.5

    # Saving the modified Excel file
    output_dir = get_output_directory()
    output_dir = Path(output_dir)
    if not output_dir.is_dir():
        output_dir.mkdir(parents=True, exist_ok=True)
    workbook.save(str(output_dir / "output.out.xls"))
    # ExEnd:1

if __name__ == "__main__":
    run()