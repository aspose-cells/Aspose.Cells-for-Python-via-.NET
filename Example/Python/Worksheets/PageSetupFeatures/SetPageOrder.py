import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, PageSetup, PrintOrderType
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/PageSetupFeatures/SetPageOrder"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Obtaining the reference of the PageSetup of the worksheet
    page_setup = workbook.worksheets[0].page_setup
    
    # Setting the printing order of the pages to over then down
    page_setup.order = PrintOrderType.OVER_THEN_DOWN
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the workbook.
    workbook.save(os.path.join(output_dir, "SetPageOrder_out.xls"))

if __name__ == "__main__":
    run()