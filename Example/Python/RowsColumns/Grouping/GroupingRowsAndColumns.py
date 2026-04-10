import os
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/Grouping/GroupingRowsAndColumns"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Creating a file stream containing the Excel file to be opened
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")

    # Opening the Excel file through the file stream
    workbook = cells.Workbook(fstream)

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]

    # Grouping first six rows (from 0 to 5) and making them hidden by passing true
    worksheet.cells.group_rows(0, 5, True)

    # Grouping first three columns (from 0 to 2) and making them hidden by passing true
    worksheet.cells.group_columns(0, 2, True)

    # Saving the modified Excel file
    workbook.save(os.path.join(data_dir, "output.xls"))

    # Closing the file stream to free all resources
    fstream.close()
    # ExEnd:1

if __name__ == "__main__":
    run()