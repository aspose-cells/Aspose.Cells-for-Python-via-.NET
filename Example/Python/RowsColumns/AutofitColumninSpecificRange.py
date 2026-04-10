import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "RowsColumns/AutofitColumninSpecificRange"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    input_path = str(data_dir / "Book1.xlsx")
    
    # Opening the Excel file
    workbook = Workbook(input_path)
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Auto-fitting the column of the worksheet (columns 4 to 6, starting from row 4)
    worksheet.auto_fit_column(4, 4, 6)
    
    # Ensure output directory exists
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    # Saving the modified Excel file
    output_path = str(output_dir / "output.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    main()