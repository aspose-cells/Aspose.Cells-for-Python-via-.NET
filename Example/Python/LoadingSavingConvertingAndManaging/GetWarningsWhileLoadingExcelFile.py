import os
from aspose.cells import Workbook, LoadOptions, IWarningCallback, WarningType
from datetime import datetime

class WarningCallback(IWarningCallback):
    def warning(self, warning_info):
        if warning_info.warning_type == WarningType.DUPLICATE_DEFINED_NAME:
            print("Duplicate Defined Name Warning: " + warning_info.description)

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "LoadingSavingConvertingAndManaging", "GetWarningsWhileLoadingExcelFile")

def get_source_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "02_OutputDirectory")

def run():
    data_dir = get_data_dir()
    
    options = LoadOptions()
    options.warning_callback = WarningCallback()
    
    input_path = os.path.join(data_dir, "sampleDuplicateDefinedName.xlsx")
    output_path = os.path.join(data_dir, "outputDuplicateDefinedName.xlsx")
    
    book = Workbook(input_path, options)
    book.save(output_path)

if __name__ == "__main__":
    run()