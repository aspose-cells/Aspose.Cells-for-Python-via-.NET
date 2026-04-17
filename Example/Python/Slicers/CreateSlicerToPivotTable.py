import os
from pathlib import Path
from aspose import cells
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color
from datetime import datetime

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())
    
    # Load sample Excel file containing pivot table.
    wb = Workbook(os.path.join(source_dir, "sampleCreateSlicerToPivotTable.xlsx"))
    
    # Access first worksheet.
    ws = wb.worksheets[0]
    
    # Access first pivot table inside the worksheet.
    pt = ws.pivot_tables[0]
    
    # Add slicer relating to pivot table with first base field at cell B22.
    idx = ws.slicers.add(pt, "B22", pt.base_fields[0])
    
    # Access the newly added slicer from slicer collection.
    # (Not used further in original code, so no additional processing needed)
    
    # Save the workbook in output XLSX format.
    wb.save(os.path.join(output_dir, "outputCreateSlicerToPivotTable.xlsx"), SaveFormat.XLSX)
    
    # Save the workbook in output XLSB format.
    wb.save(os.path.join(output_dir, "outputCreateSlicerToPivotTable.xlsb"), SaveFormat.XLSB)

if __name__ == "__main__":
    main()