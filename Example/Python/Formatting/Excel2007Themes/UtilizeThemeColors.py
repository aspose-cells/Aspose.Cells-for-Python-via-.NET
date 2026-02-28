import os
from aspose.cells import Workbook, Cells, Cell, Style, BackgroundType, ThemeColorType, ThemeColor
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/Excel2007Themes/UtilizeThemeColors"

def run():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    workbook = Workbook()
    
    cells = workbook.worksheets[0].cells
    
    c = cells.get("D3")
    
    s = c.get_style()
    
    s.foreground_theme_color = ThemeColor(ThemeColorType.ACCENT2, 0.5)
    
    s.pattern = BackgroundType.SOLID
    
    f = s.font
    
    f.theme_color = ThemeColor(ThemeColorType.ACCENT4, 0.1)
    
    c.set_style(s)
    
    c.put_value("Testing1")
    
    workbook.save(str(data_dir / "output.out.xlsx"))

if __name__ == "__main__":
    run()