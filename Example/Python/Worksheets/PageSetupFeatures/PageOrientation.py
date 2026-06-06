from aspose.cells import Workbook, PageOrientationType
from pathlib import Path
import os

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "PageOrientation"

def run():
    data_dir = get_data_dir()
    
    # Ensure the output directory exists
    os.makedirs(str(data_dir), exist_ok=True)
    
    workbook = Workbook()
    
    worksheet = workbook.worksheets[0]
    
    worksheet.page_setup.orientation = PageOrientationType.PORTRAIT
    
    output_path = os.path.join(str(data_dir), "PageOrientation_out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run()