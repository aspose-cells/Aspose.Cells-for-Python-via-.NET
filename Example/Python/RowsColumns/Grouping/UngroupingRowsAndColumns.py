import os
import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "RowsColumns/Grouping/UngroupingRowsAndColumns")

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(os.path.join(data_dir, "book1.xls"))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.ungroup_rows(0, 5)
    
    worksheet.cells.ungroup_columns(0, 2)
    
    workbook.save(os.path.join(data_dir, "output.xls"))

if __name__ == "__main__":
    run()