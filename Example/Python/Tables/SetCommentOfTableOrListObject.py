import os
from aspose.cells import Workbook, SaveFormat
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Tables/SetCommentOfTableOrListObject"

def main():
    data_dir = get_data_dir()
    
    # Open the template file
    workbook = Workbook(str(data_dir / "source.xlsx"))
    
    # Access first worksheet
    worksheet = workbook.worksheets[0]
    
    # Access first list object or table
    lst_obj = worksheet.list_objects[0]
    
    # Set the comment of the list object
    lst_obj.comment = "This is Aspose.Cells comment."
    
    # Save the workbook in xlsx format
    output_path = str(data_dir / "SetCommentOfTableOrListObject_out.xlsx")
    workbook.save(output_path, SaveFormat.XLSX)

if __name__ == "__main__":
    main()