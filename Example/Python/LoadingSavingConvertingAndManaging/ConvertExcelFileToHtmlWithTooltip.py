import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "LoadingSavingConvertingAndManaging/ConvertExcelFileToHtmlWithTooltip"

def convert_excel_file_to_html_with_tooltip():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    workbook = cells.Workbook(str(source_dir / "AddTooltipToHtmlSample.xlsx"))
    
    options = cells.HtmlSaveOptions()
    options.add_tooltip_text = True
    
    workbook.save(str(output_dir / "AddTooltipToHtmlSample_out.html"), options)

if __name__ == "__main__":
    convert_excel_file_to_html_with_tooltip()