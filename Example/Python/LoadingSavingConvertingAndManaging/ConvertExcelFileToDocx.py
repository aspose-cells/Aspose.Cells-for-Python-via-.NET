import os
from pathlib import Path
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def convert_excel_file_to_docx():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Open the template file
    workbook = cells.Workbook(str(source_dir / "Book1.xlsx"))
    
    # Save as Docx
    workbook.save(str(output_dir / "Book1.docx"), cells.SaveFormat.DOCX)
    
    print("ConvertExcelFileToDocx executed successfully.")

if __name__ == "__main__":
    convert_excel_file_to_docx()