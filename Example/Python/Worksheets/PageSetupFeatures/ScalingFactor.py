import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "ScalingFactor"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook()
    
    worksheet = workbook.worksheets[0]
    
    worksheet.page_setup.zoom = 100
    
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    workbook.save(str(output_dir / "ScalingFactor_out.xls"))

if __name__ == "__main__":
    run()