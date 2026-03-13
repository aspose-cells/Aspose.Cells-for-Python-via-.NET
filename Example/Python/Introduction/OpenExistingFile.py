import os
import sys
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    fstream = open(os.path.join(source_dir, "sampleOpenExistingFile.xlsx"), "rb")
    
    workbook = cells.Workbook(fstream)
    
    cell = workbook.worksheets[0].cells.get("A1")
    cell.put_value("Hello World!")
    
    workbook.save(os.path.join(output_dir, "outputOpenExistingFile.xlsx"))
    
    fstream.close()
    
    print("OpenExistingFile executed successfully.\r\n")

if __name__ == "__main__":
    run()