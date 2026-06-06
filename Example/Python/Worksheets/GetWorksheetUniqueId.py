import os
from pathlib import Path
from aspose.cells import Workbook
from datetime import datetime

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def main():
    source_dir = get_source_directory()
    
    workbook = Workbook(os.path.join(source_dir, "Book1.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    print(f"Unique Id: {worksheet.unique_id}")
    
    print("GetWorksheetUniqueId executed successfully.")

if __name__ == "__main__":
    main()