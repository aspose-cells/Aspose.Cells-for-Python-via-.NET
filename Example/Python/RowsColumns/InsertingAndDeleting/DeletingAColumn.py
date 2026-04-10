import os
from pathlib import Path
from aspose import pydrawing as drawing
from aspose.cells import Workbook
from datetime import datetime

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/DeletingAColumn"

def main():
    data_dir = get_data_dir()
    
    fstream = open(os.path.join(data_dir, "Book1.xlsx"), "rb")
    
    workbook = Workbook(fstream)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.delete_column(4)
    
    output_path = os.path.join(data_dir, "output.xlsx")
    workbook.save(output_path)
    
    fstream.close()

if __name__ == "__main__":
    main()