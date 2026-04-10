import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/DeletingARow"

def main():
    data_dir = get_data_dir()
    
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    workbook = cells.Workbook(fstream)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.delete_row(2)
    
    workbook.save(os.path.join(data_dir, "output.out.xls"))
    
    fstream.close()

if __name__ == "__main__":
    main()