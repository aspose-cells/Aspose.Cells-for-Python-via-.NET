import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/DealingWithFontSettings/SettingSubScriptEffect"

def setting_sub_script_effect():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    workbook = Workbook()
    
    i = workbook.worksheets.add()
    worksheet = workbook.worksheets[i]
    
    cell = worksheet.cells.get("A1")
    cell.put_value("Hello Aspose!")
    
    style = cell.get_style()
    style.font.is_subscript = True
    cell.set_style(style)
    
    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path, SaveFormat.EXCEL_97_TO_2003)

setting_sub_script_effect()