import aspose.cells as cells
from datetime import datetime
from pathlib import Path
import os

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample Excel file containing a table.
    workbook = cells.Workbook(str(source_dir / "sampleCreateSlicerToExcelTable.xlsx"))
    
    # Access first worksheet.
    worksheet = workbook.worksheets[0]
    
    # Access first table inside the worksheet.
    table = worksheet.list_objects[0]
    
    # Add slicer
    idx = worksheet.slicers.add(table, 0, "H5")
    
    # Save the workbook in output XLSX format.
    output_path = str(output_dir / "outputCreateSlicerToExcelTable.xlsx")
    workbook.save(output_path, cells.SaveFormat.XLSX)
    
    print("CreateSlicerToExcelTable executed successfully.")

if __name__ == "__main__":
    main()