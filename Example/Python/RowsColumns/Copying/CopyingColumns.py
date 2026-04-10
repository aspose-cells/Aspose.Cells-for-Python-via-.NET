import os
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "RowsColumns", "Copying", "CopyingColumns")


def run():
    data_dir = get_data_dir()
    
    # Create another Workbook.
    excel_workbook1 = cells.Workbook(os.path.join(data_dir, "book1.xls"))
    
    # Get the first worksheet in the book.
    ws1 = excel_workbook1.worksheets[0]
    
    # Copy the first column from the first worksheet into the third column (index 2)
    ws1.cells.copy_column(ws1.cells, 0, 2)
    
    # Autofit the column.
    ws1.auto_fit_column(2)
    
    # Save the excel file.
    excel_workbook1.save(os.path.join(data_dir, "output.xls"))


if __name__ == "__main__":
    run()