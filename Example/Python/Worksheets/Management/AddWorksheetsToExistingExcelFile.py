from aspose.cells import Workbook
from aspose.pydrawing import Color
import os
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Management/AddWorksheetsToExistingExcelFile"

def main():
    data_dir = get_data_dir()
    
    # Instantiating a Workbook object
    # Opening the Excel file
    workbook = Workbook(str(data_dir / "book1.xls"))
    
    # Adding a new worksheet to the Workbook object
    i = workbook.worksheets.add()
    
    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]
    
    # Setting the name of the newly added worksheet
    worksheet.name = "My Worksheet"
    
    # Saving the Excel file
    output_path = data_dir / "output.out.xls"
    workbook.save(str(output_path))

if __name__ == "__main__":
    main()