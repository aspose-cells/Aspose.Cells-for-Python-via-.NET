import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/InsertingARow"

def run():
    data_dir = get_data_dir()
    
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    workbook = cells.Workbook(fstream)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.insert_row(2)
    
    output_path = os.path.join(data_dir, "output.out.xls")
    workbook.save(output_path)
    
    fstream.close()

if __name__ == "__main__":
    run()