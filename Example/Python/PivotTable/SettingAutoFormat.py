import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.cells.pivot import PivotTableAutoFormatType
from pathlib import Path


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "SettingAutoFormat"


def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(str(data_dir / "Book1.xls"))
    
    pivot_index = 0
    
    worksheet = workbook.worksheets[0]
    
    pivot_table = worksheet.pivot_tables[pivot_index]
    
    pivot_table.is_auto_format = True
    pivot_table.auto_format_type = PivotTableAutoFormatType.REPORT5
    
    workbook.save(str(data_dir / "output.xls"))


if __name__ == "__main__":
    run()