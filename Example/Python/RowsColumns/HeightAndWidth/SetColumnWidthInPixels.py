import os
from aspose import pydrawing as drawing
import aspose.cells as cells
from datetime import datetime
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def set_column_width_in_pixels():
    source_dir = get_source_directory()
    out_dir = get_output_directory()
    
    # Load source Excel file
    workbook = cells.Workbook(os.path.join(source_dir, "Book1.xlsx"))
    
    # Access first worksheet
    worksheet = workbook.worksheets[0]
    
    # Set the width of the column in pixels
    worksheet.cells.set_column_width_pixel(7, 200)
    
    workbook.save(os.path.join(out_dir, "SetColumnWidthInPixels_Out.xlsx"))
    
    print("SetColumnWidthInPixels executed successfully.")

if __name__ == "__main__":
    set_column_width_in_pixels()