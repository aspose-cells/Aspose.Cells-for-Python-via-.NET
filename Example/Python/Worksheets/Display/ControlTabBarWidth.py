import os
from datetime import datetime
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/ControlTabBarWidth"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    
    workbook = cells.Workbook(str(data_dir / "book1.xls"))
    
    workbook.settings.show_tabs = True
    workbook.settings.sheet_tab_bar_width = 800
    
    output_dir = get_output_directory()
    os.makedirs(str(output_dir), exist_ok=True)
    
    workbook.save(str(output_dir / "output.xls"))

if __name__ == "__main__":
    main()