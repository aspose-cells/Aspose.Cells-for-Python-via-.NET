import os
from aspose.cells import Workbook
from aspose.cells.tables import ListObjectCollection, TotalsCalculation
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Tables/CreatingListObject"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Create a Workbook object.
    # Open a template excel file.
    workbook = Workbook(str(data_dir / "book1.xls"))

    # Get the List objects collection in the first worksheet.
    list_objects = workbook.worksheets[0].list_objects

    # Add a List based on the data source range with headers on.
    list_objects.add(1, 1, 7, 5, True)

    # Show the total row for the List.
    list_objects[0].show_totals = True

    # Calculate the total of the last (5th ) list column.
    list_objects[0].list_columns[4].totals_calculation = TotalsCalculation.SUM

    # Save the excel file.
    workbook.save(str(data_dir / "output.xls"))
    # ExEnd:1

if __name__ == "__main__":
    run()