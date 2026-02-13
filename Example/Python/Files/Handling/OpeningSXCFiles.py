import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

source_dir = get_source_directory()
workbook = cells.Workbook(str(source_dir / "SampleSXC.sxc"))
worksheet = workbook.worksheets[0]
cell = worksheet.cells.get("C3")
print(f"Cell Name: {cell.name} Value: {cell.string_value}")
print("OpeningSXCFiles executed successfully!")