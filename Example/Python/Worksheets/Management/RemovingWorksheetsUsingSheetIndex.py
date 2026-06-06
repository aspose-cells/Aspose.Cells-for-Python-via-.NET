import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory(): 
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory(): 
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Management/RemovingWorksheetsUsingSheetIndex"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Creating a file stream containing the Excel file to be opened
    fstream = open(str(data_dir / "book1.xls"), "rb")

    # Instantiating a Workbook object
    # Opening the Excel file through the file stream
    workbook = Workbook(fstream)

    # Removing a worksheet using its sheet index
    del workbook.worksheets[0]

    # Save workbook
    workbook.save(str(data_dir / "output.out.xls"))
    # ExEnd:1

if __name__ == "__main__":
    run()