import os
from aspose.cells import Workbook
from aspose.cells.pivot import PivotFieldDataDisplayFormat, PivotItemPosition
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "SettingDataFieldFormat"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(str(data_dir / "Book1.xls"))
    
    worksheet = workbook.worksheets[0]
    pivot_index = 0
    
    pivot_table = worksheet.pivot_tables[pivot_index]
    pivot_fields = pivot_table.data_fields
    
    pivot_field = pivot_fields[0]
    
    pivot_field.data_display_format = PivotFieldDataDisplayFormat.PERCENTAGE_OF
    pivot_field.base_field_index = 1
    pivot_field.base_item_position = PivotItemPosition.NEXT
    pivot_field.number = 10
    
    workbook.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    run()