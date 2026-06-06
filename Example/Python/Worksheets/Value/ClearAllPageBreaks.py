import os
from pathlib import Path
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/ClearAllPageBreaks"

def run():
    data_dir = get_data_dir()
    
    # Ensure the directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    workbook = Workbook()
    
    workbook.worksheets[0].horizontal_page_breaks.clear()
    workbook.worksheets[0].vertical_page_breaks.clear()
    
    output_path = os.path.join(data_dir, "ClearAllPageBreaks_out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run()