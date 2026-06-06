import os
from pathlib import Path
from aspose.cells import Workbook
from datetime import datetime

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "FitToPagesOptions"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def fit_to_pages_options():
    data_dir = get_data_dir()
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Setting the number of pages to which the length of the worksheet will be spanned
    worksheet.page_setup.fit_to_pages_tall = 1
    
    # Setting the number of pages to which the width of the worksheet will be spanned
    worksheet.page_setup.fit_to_pages_wide = 1
    
    # Ensure output directory exists
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    # Save the workbook.
    output_file = os.path.join(output_dir, "FitToPagesOptions_out.xls")
    workbook.save(output_file)

if __name__ == "__main__":
    fit_to_pages_options()