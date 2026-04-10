import os
from pathlib import Path
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns" / "HeightAndWidth" / "SettingHeightOfRow"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    os.makedirs(output_dir, exist_ok=True)
    
    workbook = Workbook(str(data_dir / "book1.xls"))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.set_row_height(1, 13.0)
    
    output_path = os.path.join(output_dir, "output.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    main()