import aspose.cells as cells
from aspose.pydrawing import Color
from datetime import datetime
import os
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "WorkbookVBAProject" / "FindoutifVBAProjectisProtected"

def run():
    # ExStart: FindoutifVBAProjectisProtected
    # Create a workbook.
    wb = cells.Workbook()

    # Access the VBA project of the workbook.
    vba_proj = wb.vba_project

    # Find out if VBA Project is Protected using IsProtected property.
    print("IsProtected - Before Protecting VBA Project: " + str(vba_proj.is_protected))

    # Protect the VBA project.
    vba_proj.protect(True, "11")

    # Find out if VBA Project is Protected using IsProtected property.
    print("IsProtected - After Protecting VBA Project: " + str(vba_proj.is_protected))
    # ExEnd: FindoutifVBAProjectisProtected

if __name__ == "__main__":
    run()