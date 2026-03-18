import os
from aspose.cells import Workbook, TxtSaveOptions
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "LoadingSavingConvertingAndManaging" / "TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # ExStart:TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat
    # The path to the documents directory.
    data_dir = get_data_dir()
    
    #Load source workbook
    wb = Workbook(str(data_dir / "sampleTrimBlankColumns.xlsx"))
    
    #Save in csv format
    wb.save(str(data_dir / "outputWithoutTrimBlankColumns.csv"))
    
    #Now save again with TrimLeadingBlankRowAndColumn as true
    opts = TxtSaveOptions()
    opts.trim_leading_blank_row_and_column = True
    
    #Save in csv format
    wb.save(str(data_dir / "outputTrimBlankColumns.csv"), opts)
    
    # ExEnd:TrimLeadingBlankRowsAndColumnsWhileExportingSpreadsheetsToCSVFormat

if __name__ == "__main__":
    run()