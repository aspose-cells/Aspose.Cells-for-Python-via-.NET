import os
from aspose.cells import Workbook, HtmlSaveOptions, HtmlCrossType
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    wb = Workbook(os.path.join(source_dir, "sampleHtmlCrossStringType.xlsx"))

    # Process each cross type - save one file per type
    cross_types = [
        (HtmlCrossType.DEFAULT, "Default"),
        (HtmlCrossType.MS_EXPORT, "MSExport"),
        (HtmlCrossType.CROSS, "Cross"),
        (HtmlCrossType.FIT_TO_CELL, "FitToCell")
    ]
    
    for cross_type, cross_type_name in cross_types:
        opts = HtmlSaveOptions()
        opts.html_cross_string_type = cross_type
        wb.save(os.path.join(output_dir, f"out{cross_type_name}.htm"), opts)

if __name__ == "__main__":
    run()