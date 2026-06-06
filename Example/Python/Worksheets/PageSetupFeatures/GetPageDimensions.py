import os
from pathlib import Path
from aspose import pydrawing as drawing
from aspose.cells import Workbook
from aspose.cells import PaperSizeType
from datetime import datetime

def get_source_directory(): 
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory(): 
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "GetPageDimensions"

def run():
    # Create an instance of Workbook class
    book = Workbook()

    # Access first worksheet
    sheet = book.worksheets[0]

    # Set paper size to A2 and print paper width and height in inches
    sheet.page_setup.paper_size = PaperSizeType.PAPER_A2
    print("PaperA2: " + str(sheet.page_setup.paper_width) + "x" + str(sheet.page_setup.paper_height))

    # Set paper size to A3 and print paper width and height in inches
    sheet.page_setup.paper_size = PaperSizeType.PAPER_A3
    print("PaperA3: " + str(sheet.page_setup.paper_width) + "x" + str(sheet.page_setup.paper_height))

    # Set paper size to A4 and print paper width and height in inches
    sheet.page_setup.paper_size = PaperSizeType.PAPER_A4
    print("PaperA4: " + str(sheet.page_setup.paper_width) + "x" + str(sheet.page_setup.paper_height))

    # Set paper size to Letter and print paper width and height in inches
    sheet.page_setup.paper_size = PaperSizeType.PAPER_LETTER
    print("PaperLetter: " + str(sheet.page_setup.paper_width) + "x" + str(sheet.page_setup.paper_height))

    print("GetPageDimensions executed successfully.\r\n")

if __name__ == "__main__":
    run()