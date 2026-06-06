import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "SetFirstPageNumber"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Setting the first page number of the worksheet pages
    worksheet.page_setup.first_page_number = 2
    
    # Save the Workbook.
    output_path = os.path.join(output_dir, "SetFirstPageNumber_out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run()