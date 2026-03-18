import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "02_OutputDirectory")

def run():
    output_dir = get_output_directory()
    
    wb = Workbook()
    
    bdpc = wb.built_in_document_properties
    
    bdpc.title = "Aspose File Format APIs"
    bdpc.author = "Aspose APIs Developers"
    bdpc.document_version = "Aspose.Cells Version - 18.3"
    
    output_file = os.path.join(output_dir, "outputSpecifyDocumentVersionOfExcelFile.xlsx")
    wb.save(output_file, SaveFormat.XLSX)
    
    print("SpecifyDocumentVersionOfExcelFile executed successfully.")

if __name__ == "__main__":
    run()