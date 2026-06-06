from aspose import cells
from aspose.cells import Workbook
import os
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "SetPrintQuality"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    # Ensure data directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Setting the print quality of the worksheet to 180 dpi
    worksheet.page_setup.print_quality = 180
    
    # Save the Workbook.
    output_path = os.path.join(data_dir, "SetPrintQuality_out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run()