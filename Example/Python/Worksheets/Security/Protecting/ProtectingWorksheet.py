import os
from aspose.cells import Workbook, SaveFormat, ProtectionType

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "02_OutputDirectory")

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "Worksheets/Security/Protecting/ProtectingWorksheet")

def run():
    data_dir = get_data_dir()
    
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    excel = Workbook(fstream)
    
    worksheet = excel.worksheets[0]
    
    worksheet.protect(ProtectionType.ALL, "aspose", None)
    
    output_path = os.path.join(data_dir, "output.out.xls")
    excel.save(output_path, SaveFormat.EXCEL_97_TO_2003)
    
    fstream.close()

if __name__ == "__main__":
    run()