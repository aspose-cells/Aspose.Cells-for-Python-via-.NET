import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/PageBreakPreview"

def run():
    data_dir = get_data_dir()
    
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    workbook = cells.Workbook(fstream)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.is_page_break_preview = True
    
    output_path = os.path.join(data_dir, "output.xls")
    workbook.save(output_path)
    
    fstream.close()

if __name__ == "__main__":
    run()