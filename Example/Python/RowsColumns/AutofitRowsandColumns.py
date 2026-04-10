import os
from datetime import datetime
from pathlib import Path
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "RowsColumns/AutofitRowsandColumns"


def run():
    data_dir = get_data_dir()
    
    input_path = str(data_dir / "Book1.xlsx")
    
    workbook = cells.Workbook(input_path)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.auto_fit_row(1)
    
    output_path = str(data_dir / "output.xlsx")
    workbook.save(output_path)


if __name__ == "__main__":
    run()