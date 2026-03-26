import os
from pathlib import Path
from aspose import cells as cells
from aspose.pydrawing import Color
from aspose.cells.pivot import PivotTableStyleType
from datetime import datetime

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "FormattingLook"

def main():
    data_dir = get_data_dir()
    
    # Load a template file
    workbook = cells.Workbook(str(data_dir / "Book1.xls"))
    
    # Get the first worksheet
    worksheet = workbook.worksheets[0]
    pivot = workbook.worksheets[0].pivot_tables[0]
    
    pivot.pivot_table_style_type = PivotTableStyleType.PIVOT_TABLE_STYLE_DARK1
    
    style = workbook.create_style()
    style.font.name = "Arial Black"
    style.foreground_color = Color.yellow
    style.pattern = cells.BackgroundType.SOLID
    
    pivot.format_all(style)
    
    # Saving the Excel file
    workbook.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    main()