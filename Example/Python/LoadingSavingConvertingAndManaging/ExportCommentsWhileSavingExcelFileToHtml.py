import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, HtmlSaveOptions
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "LoadingSavingConvertingAndManaging/ExportCommentsWhileSavingExcelFileToHtml"

def export_comments_while_saving_excel_file_to_html():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample Excel file
    wb = Workbook(os.path.join(source_dir, "sampleExportCommentsHTML.xlsx"))
    
    # Export comments - set IsExportComments property to true
    opts = HtmlSaveOptions()
    opts.is_export_comments = True
    
    # Save the Excel file to HTML
    wb.save(os.path.join(output_dir, "outputExportCommentsHTML.html"), opts)

if __name__ == "__main__":
    export_comments_while_saving_excel_file_to_html()