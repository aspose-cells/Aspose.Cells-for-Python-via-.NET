import os
from aspose.pydrawing import Color
import aspose.cells as cells
from pathlib import Path


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/RemoveSpecificPageBreak"


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


def run():
    data_dir = get_data_dir()
    
    workbook = cells.Workbook(os.path.join(data_dir, "PageBreaks.xls"))
    
    workbook.worksheets[0].horizontal_page_breaks.remove(workbook.worksheets[0].horizontal_page_breaks[0])
    workbook.worksheets[0].vertical_page_breaks.remove(workbook.worksheets[0].vertical_page_breaks[0])
    
    output_path = os.path.join(data_dir, "RemoveSpecificPageBreak_out.xls")
    workbook.save(output_path)


if __name__ == "__main__":
    run()