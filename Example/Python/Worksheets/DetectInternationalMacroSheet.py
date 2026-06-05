import os
from datetime import datetime
from pathlib import Path
from aspose import cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Worksheets/DetectInternationalMacroSheet"

def run():
    source_dir = str(get_source_directory())
    
    workbook = cells.Workbook(os.path.join(source_dir, "InternationalMacroSheet.xlsm"))
    
    sheet_type = workbook.worksheets[0].type
    
    print("Sheet Type: " + str(sheet_type))
    
    print("DetectInternationalMacroSheet executed successfully.")

if __name__ == "__main__":
    run()