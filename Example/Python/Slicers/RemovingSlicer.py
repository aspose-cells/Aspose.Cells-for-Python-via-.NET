import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat
from datetime import datetime
from pathlib import Path


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"


def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample Excel file containing slicer.
    wb = Workbook(os.path.join(source_dir, "sampleRemovingSlicer.xlsx"))
    
    # Access first worksheet.
    ws = wb.worksheets[0]
    
    # Access the first slicer inside the slicer collection.
    slicer = ws.slicers[0]
    
    # Remove slicer.
    ws.slicers.remove(slicer)
    
    # Save the workbook in output XLSX format.
    wb.save(os.path.join(output_dir, "outputRemovingSlicer.xlsx"), SaveFormat.XLSX)
    
    print("RemovingSlicer executed successfully.")


if __name__ == "__main__":
    main()