import os
from aspose.cells import Workbook
from datetime import datetime

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "RowsColumns/Hiding/HidingMultipleRowsAndColumns")

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "02_OutputDirectory")

def main():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    workbook = Workbook(os.path.join(data_dir, "book1.xls"))
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.hide_rows(2, 3)
    worksheet.cells.hide_columns(1, 2)
    
    workbook.save(os.path.join(output_dir, "outputxls"))

if __name__ == "__main__":
    main()