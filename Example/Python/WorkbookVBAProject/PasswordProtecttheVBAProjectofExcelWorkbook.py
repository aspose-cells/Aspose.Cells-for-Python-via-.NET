import os
from pathlib import Path
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "WorkbookVBAProject/PasswordProtecttheVBAProjectofExcelWorkbook"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load your source Excel file.
    wb = Workbook(str(data_dir / "samplePasswordProtectVBAProject.xlsm"))
    
    # Access the VBA project of the workbook.
    vba_project = wb.vba_project
    
    # Lock the VBA project for viewing with password.
    vba_project.protect(True, "11")
    
    # Save the output Excel file
    wb.save(str(data_dir / "outputPasswordProtectVBAProject.xlsm"))

if __name__ == "__main__":
    main()