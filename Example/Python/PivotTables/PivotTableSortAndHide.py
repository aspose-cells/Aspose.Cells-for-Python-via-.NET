import os
from aspose.cells import Workbook
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    workbook = Workbook(str(source_dir / "PivotTableHideAndSortSample.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    pivot_table = worksheet.pivot_tables[0]
    data_body_range = pivot_table.data_body_range
    current_row = 3
    rows_used = data_body_range.end_row
    
    field = pivot_table.row_fields[0]
    field.is_auto_sort = True
    field.is_ascend_sort = False
    field.auto_sort_field = 0
    
    pivot_table.refresh_data()
    pivot_table.calculate_data()
    
    while current_row < rows_used:
        cell = worksheet.cells.get(current_row, 1)
        score = float(cell.value)
        if score < 60:
            worksheet.cells.hide_row(current_row)
        current_row += 1
    
    pivot_table.refresh_data()
    pivot_table.calculate_data()
    
    workbook.save(str(output_dir / "PivotTableHideAndSort_out.xlsx"))

if __name__ == "__main__":
    run()