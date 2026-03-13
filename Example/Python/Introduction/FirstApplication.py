import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # Output directory
    output_dir = get_output_directory()
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Instantiate a Workbook object that represents Excel file.
    wb = Workbook()
    
    # When you create a new workbook, a default "Sheet1" is added to the workbook.
    sheet = wb.worksheets[0]
    
    # Access the "A1" cell in the sheet.
    cell = sheet.cells.get("A1")
    
    # Input the "Hello World!" text into the "A1" cell
    cell.put_value("Hello World!")
    
    # Save the Excel file.
    output_path = os.path.join(output_dir, "outputFirstApplication.xlsx")
    wb.save(output_path, SaveFormat.XLSX)
    
    print("FirstApplication executed successfully.\r\n")

if __name__ == "__main__":
    run()