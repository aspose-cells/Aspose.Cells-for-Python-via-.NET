import aspose.cells as cells
import os
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
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
    
    slicer = worksheet.slicers[idx]
    # In Aspose.Cells for Python, PlacementType is accessed via the enum in the drawing module
    import aspose.cells.drawing as drawing
    slicer.placement = drawing.PlacementType.FREE_FLOATING
    slicer.row_height_pixel = 50
    slicer.width_pixel = 500
    slicer.title = "Aspose"
    slicer.alternative_text = "Alternate Text"
    slicer.is_printable = False
    slicer.is_locked = False
    
    # Refresh the slicer.
    slicer.refresh()
    
    # Save the workbook in output XLSX format.
    workbook.save(str(output_dir / "outputChangeSlicerProperties.xlsx"), cells.SaveFormat.XLSX)

if __name__ == "__main__":
    run()