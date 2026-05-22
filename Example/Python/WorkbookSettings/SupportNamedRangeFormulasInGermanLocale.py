import os
from aspose.cells import Workbook
from datetime import datetime
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "WorkbookSettings/SupportNamedRangeFormulasInGermanLocale"

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    data_dir = get_data_dir()
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # ExStart:1
    name = "HasFormula"
    value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

    wb_source = Workbook(str(source_dir / "sampleNamedRangeTest.xlsm"))
    ws_col = wb_source.worksheets

    name_index = ws_col.names.add(name)
    named_range = ws_col.names[name_index]
    named_range.refers_to = value

    wb_source.save(str(output_dir / "sampleOutputNamedRangeTest.xlsm"))
    # ExEnd:1
    print("SupportNamedRangeFormulasInGermanLocale executed successfully.\r\n")

if __name__ == "__main__":
    main()