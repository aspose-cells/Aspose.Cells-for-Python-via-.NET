import os
from pathlib import Path
from datetime import datetime
import aspose.pydrawing as drawing
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "RowsColumns/AutofitRowinSpecificRange"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    input_path = str(data_dir / "Book1.xlsx")
    
    workbook = cells.Workbook(input_path)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.auto_fit_row(1, 0, 5)
    
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = str(output_dir / "output.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    main()