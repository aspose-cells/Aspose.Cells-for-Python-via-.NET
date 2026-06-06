import os
from datetime import datetime
from pathlib import Path
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Management/AddingWorksheetsToNewExcelFile"


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


def run():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    workbook = cells.Workbook()
    
    i = workbook.worksheets.add()
    
    worksheet = workbook.worksheets[i]
    
    worksheet.name = "My Worksheet"
    
    workbook.save(str(data_dir / "output.out.xls"))


if __name__ == "__main__":
    run()