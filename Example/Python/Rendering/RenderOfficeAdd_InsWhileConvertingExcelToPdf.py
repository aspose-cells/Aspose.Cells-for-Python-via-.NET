import os
from pathlib import Path
from datetime import datetime
from aspose import pydrawing
import aspose.cells as cells
from aspose.cells import CellsHelper

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    wb = cells.Workbook(str(source_dir / "sampleRenderOfficeAdd-Ins.xlsx"))
    
    output_filename = f"output-{CellsHelper.get_version()}.pdf"
    wb.save(str(output_dir / output_filename))
    
    print("RenderOfficeAdd_InsWhileConvertingExcelToPdf executed successfully.")

if __name__ == "__main__":
    run()