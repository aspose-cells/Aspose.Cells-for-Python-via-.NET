import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook, PaperSizeType
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "ManagePaperSize"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    
    workbook = Workbook()
    
    worksheet = workbook.worksheets[0]
    
    worksheet.page_setup.paper_size = PaperSizeType.PAPER_A4
    
    output_dir = get_output_directory()
    output_file = os.path.join(output_dir, "ManagePaperSize_out.xls")
    workbook.save(output_file)

if __name__ == "__main__":
    main()