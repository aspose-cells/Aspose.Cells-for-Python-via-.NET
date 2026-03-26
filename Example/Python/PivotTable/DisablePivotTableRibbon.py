import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.cells.pivot import PivotTable

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTable/DisablePivotTableRibbon"

if __name__ == "__main__":
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    wb = Workbook(str(source_dir / "samplePivotTableTest.xlsx"))
    
    pt = wb.worksheets[0].pivot_tables[0]
    
    pt.enable_wizard = False
    
    wb.save(str(output_dir / "outputSamplePivotTableTest.xlsx"))

    print("DisablePivotTableRibbon executed successfully.\r\n")