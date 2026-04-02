import os
from datetime import datetime
from aspose.cells import LoadOptions, Workbook
from aspose.cells.pivot import PivotTable

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    options = LoadOptions()
    options.parsing_pivot_cached_records = True
    
    wb = Workbook(os.path.join(source_dir, "sampleParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx"), options)
    
    ws = wb.worksheets[0]
    pt = ws.pivot_tables[0]
    
    pt.refresh_data_flag = True
    pt.refresh_data()
    pt.calculate_data()
    pt.refresh_data_flag = False
    
    wb.save(os.path.join(output_dir, "outputParsingPivotCachedRecordsWhileLoadingExcelFile.xlsx"))

if __name__ == "__main__":
    run()