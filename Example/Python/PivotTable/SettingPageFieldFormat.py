import os
from datetime import datetime
from pathlib import Path
from aspose import cells
from aspose.cells import Workbook
from aspose.cells.pivot import PivotFieldType, PivotFieldSubtotalType
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "SettingPageFieldFormat"

def main():
    data_dir = get_data_dir()
    
    workbook = Workbook(str(data_dir / "Book1.xls"))
    
    worksheet = workbook.worksheets[0]
    pivotindex = 0
    
    pivot_table = worksheet.pivot_tables[pivotindex]
    
    pivot_table.row_grand = True
    
    pivot_fields = pivot_table.row_fields
    
    pivot_field = pivot_fields[0]
    
    pivot_field.set_subtotals(PivotFieldSubtotalType.SUM, True)
    pivot_field.set_subtotals(PivotFieldSubtotalType.COUNT, True)
    
    pivot_field.is_auto_sort = True
    
    pivot_field.is_ascend_sort = True
    
    pivot_field.auto_sort_field = -5
    
    pivot_field.is_auto_show = True
    
    pivot_field.is_ascend_show = False
    
    pivot_field.auto_show_field = 0
    
    workbook.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    main()