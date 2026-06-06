import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Management/AddingWorksheetsToDesignerSpreadSheet"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    input_path = os.path.join(str(data_dir), "book1.xlsx")
    
    workbook = cells.Workbook(input_path)
    
    i = workbook.worksheets.add()
    worksheet = workbook.worksheets[i]
    worksheet.name = "My Worksheet"
    
    output_path = os.path.join(str(get_output_directory()), "output.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    main()