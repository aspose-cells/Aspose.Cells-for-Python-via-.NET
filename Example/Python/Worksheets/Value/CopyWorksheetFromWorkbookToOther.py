import os
from pathlib import Path
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/CopyWorksheetFromWorkbookToOther"

def main():
    data_dir = get_data_dir()
    
    # Ensure output directory exists
    os.makedirs(str(data_dir), exist_ok=True)
    
    # Create a new Workbook.
    excel_workbook0 = Workbook()
    
    # Get the first worksheet in the book.
    ws0 = excel_workbook0.worksheets[0]
    
    # Put some data into header rows (A1:A4)
    for i in range(5):
        ws0.cells.get(i, 0).put_value(f"Header Row {i}")
    
    # Put some detail data (A5:A999)
    for i in range(5, 1000):
        ws0.cells.get(i, 0).put_value(f"Detail Row {i}")
    
    # Define a pagesetup object based on the first worksheet.
    pagesetup = ws0.page_setup
    
    # The first five rows are repeated in each page...
    # It can be seen in print preview.
    pagesetup.print_title_rows = "$1:$5"
    
    # Create another Workbook.
    excel_workbook1 = Workbook()
    
    # Get the first worksheet in the book.
    ws1 = excel_workbook1.worksheets[0]
    
    # Name the worksheet.
    ws1.name = "MySheet"
    
    # Copy data from the first worksheet of the first workbook into the
    # first worksheet of the second workbook.
    ws1.copy(ws0)
    
    # Save the excel file.
    output_path = os.path.join(str(data_dir), "CopyWorksheetFromWorkbookToOther_out.xls")
    excel_workbook1.save(output_path)

if __name__ == "__main__":
    main()