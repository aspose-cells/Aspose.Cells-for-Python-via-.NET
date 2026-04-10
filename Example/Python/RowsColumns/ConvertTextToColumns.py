import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, TxtLoadOptions
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "RowsColumns/ConvertTextToColumns"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Create a workbook
    wb = Workbook()
    
    # Access first worksheet
    ws = wb.worksheets[0]
    
    # Add people name in column A. First name and Last name are separated by space
    ws.cells.get("A1").put_value("John Teal")
    ws.cells.get("A2").put_value("Peter Graham")
    ws.cells.get("A3").put_value("Brady Cortez")
    ws.cells.get("A4").put_value("Mack Nick")
    ws.cells.get("A5").put_value("Hsu Lee")
    
    # Create text load options with space as separator
    opts = TxtLoadOptions()
    opts.separator = ' '
    
    # Split the column A into two columns using TextToColumns() method
    ws.cells.text_to_columns(0, 0, 5, opts)
    
    # Save the workbook in xlsx format
    output_path = os.path.join(output_dir, "outputTextToColumns.xlsx")
    wb.save(output_path)

if __name__ == "__main__":
    main()