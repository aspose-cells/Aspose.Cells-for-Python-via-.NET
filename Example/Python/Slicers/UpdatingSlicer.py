import os
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color
from datetime import datetime

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample Excel file containing slicer.
    wb = Workbook(os.path.join(source_dir, "sampleUpdatingSlicer.xlsx"))
    
    # Access first worksheet.
    ws = wb.worksheets[0]
    
    # Access the first slicer inside the slicer collection.
    slicer = ws.slicers[0]
    
    # Access the slicer items.
    sc_items = slicer.slicer_cache.slicer_cache_items
    
    # Unselect 2nd and 3rd slicer items.
    sc_items[1].selected = False
    sc_items[2].selected = False
    
    # Refresh the slicer.
    slicer.refresh()
    
    # Save the workbook in output XLSX format.
    wb.save(os.path.join(output_dir, "outputUpdatingSlicer.xlsx"), SaveFormat.XLSX)

if __name__ == "__main__":
    main()