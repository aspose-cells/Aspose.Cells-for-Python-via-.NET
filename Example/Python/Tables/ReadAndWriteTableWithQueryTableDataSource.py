import os
from aspose.cells import Workbook
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    workbook = Workbook(str(source_dir / "SampleTableWithQueryTable.xls"))
    
    worksheet = workbook.worksheets[0]
    
    table = worksheet.list_objects[0]
    
    if table.data_source_type == 2:  # QueryTable = 2 in Aspose.Cells
        table.show_totals = True
    
    workbook.save(str(output_dir / "SampleTableWithQueryTable_out.xls"))

if __name__ == "__main__":
    run()