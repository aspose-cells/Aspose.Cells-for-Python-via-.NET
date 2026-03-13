import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Introduction" / "CheckVersionNumber"

def run():
    print("Aspose.Cells for Python via .NET Version: " + cells.CellsHelper.get_version())
    print("CheckVersionNumber executed successfully.\r\n")

if __name__ == "__main__":
    run()