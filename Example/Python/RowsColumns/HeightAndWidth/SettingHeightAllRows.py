import os
from aspose import cells as cells
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/HeightAndWidth/SettingHeightAllRows"

def main():
    data_dir = get_data_dir()
    
    file_path = os.path.join(data_dir, "book1.xls")
    output_path = os.path.join(data_dir, "output.out.xls")
    
    workbook = cells.Workbook(file_path)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.standard_height = 15.0
    
    workbook.save(output_path)

if __name__ == "__main__":
    main()