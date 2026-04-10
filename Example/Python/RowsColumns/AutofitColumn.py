import os
from datetime import datetime
from pathlib import Path
from aspose import pydrawing as drawing
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "RowsColumns/AutofitColumn"

def main():
    data_dir = get_data_dir()
    input_path = os.path.join(data_dir, "Book1.xlsx")
    
    workbook = cells.Workbook(input_path)
    worksheet = workbook.worksheets[0]
    
    worksheet.auto_fit_column(4)
    
    output_path = os.path.join(data_dir, "output.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    main()