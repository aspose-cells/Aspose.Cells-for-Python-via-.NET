import os
from aspose.cells import Workbook
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "SetPrintArea"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()
    
    # Ensure the output directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Obtaining the reference of the PageSetup of the worksheet
    page_setup = workbook.worksheets[0].page_setup
    
    # Specifying the cells range (from A1 cell to T35 cell) of the print area
    page_setup.print_area = "A1:T35"
    
    # Save the workbook.
    output_path = os.path.join(data_dir, "SetPrintArea_out.xls")
    workbook.save(output_path)
    # ExEnd:1

if __name__ == "__main__":
    run()