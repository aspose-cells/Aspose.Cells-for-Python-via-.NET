import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns" / "HeightAndWidth" / "SettingHeightOfAllRowsInWorksheet"

def run():
    data_dir = get_data_dir()
    
    workbook = cells.Workbook(str(os.path.join(data_dir, "book1.xls")))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.standard_height = 15.0
    
    output_dir = Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"
    output_dir.mkdir(parents=True, exist_ok=True)
    workbook.save(str(os.path.join(output_dir, "output.out.xls")))

if __name__ == "__main__":
    run()