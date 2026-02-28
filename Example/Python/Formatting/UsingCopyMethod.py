import os
from aspose.cells import Workbook, BorderType
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "Formatting/UsingCopyMethod")

def run():
    # ExStart:1
    data_dir = get_data_dir()

    # Opening the Excel file
    workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))

    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]

    total_row_count = 0

    for i in range(workbook.worksheets.count):
        source_sheet = workbook.worksheets[i]
        source_range = source_sheet.cells.max_display_range
        
        dest_range = worksheet.cells.create_range(
            source_range.first_row + total_row_count, 
            source_range.first_column,
            source_range.row_count, 
            source_range.column_count
        )
        
        dest_range.copy(source_range)
        total_row_count = source_range.row_count + total_row_count

    # Saving the modified Excel file
    workbook.save(os.path.join(data_dir, "output.xls"))
    # ExEnd:1