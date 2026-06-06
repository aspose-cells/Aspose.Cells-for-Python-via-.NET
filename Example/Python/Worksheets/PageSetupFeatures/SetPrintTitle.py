import os
from aspose.cells import Workbook
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "SetPrintTitle"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()
    output_dir = get_output_directory()

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Instantiating a Workbook object
    workbook = Workbook()

    # Obtaining the reference of the PageSetup of the worksheet
    page_setup = workbook.worksheets[0].page_setup

    # Defining column numbers A & B as title columns
    page_setup.print_title_columns = "$A:$B"

    # Defining row numbers 1 & 2 as title rows
    page_setup.print_title_rows = "$1:$2"

    # Save the workbook.
    output_path = os.path.join(output_dir, "SetPrintTitle_out.xls")
    workbook.save(output_path)
    # ExEnd:1


if __name__ == "__main__":
    run()