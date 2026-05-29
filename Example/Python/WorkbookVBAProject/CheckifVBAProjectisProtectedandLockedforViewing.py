import os
import sys
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "WorkbookVBAProject/CheckifVBAProjectisProtectedandLockedforViewing"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    wb = Workbook(str(data_dir / "sampleCheckifVBAProjectisProtected.xlsm"))
    
    vba_project = wb.vba_project
    
    print("Is VBA Project Locked for Viewing: " + str(vba_project.islocked_for_viewing))

if __name__ == "__main__":
    run()