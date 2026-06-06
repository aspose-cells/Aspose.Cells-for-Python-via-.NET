import os
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook, Worksheet, SheetType

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def Run():
    source_dir = get_source_directory()
    
    file_path = os.path.join(source_dir, "sampleFindIfWorksheetIsDialogSheet.xlsx")
    wb = Workbook(file_path)
    
    ws = wb.worksheets[0]
    
    if ws.type == SheetType.DIALOG:
        print("Worksheet is a Dialog Sheet.")
    
    print("FindIfWorksheetIsDialogSheet executed successfully.")

if __name__ == "__main__":
    Run()