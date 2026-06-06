import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "SetMargins"

def ensure_directory_exists(path):
    path = Path(path)
    if not path.exists():
        os.makedirs(path)

def run():
    # ExStart:1
    data_dir = get_data_dir()
    
    # Ensure the output directory exists
    ensure_directory_exists(data_dir)
    
    workbook = Workbook()
    worksheets = workbook.worksheets
    worksheet = worksheets[0]
    page_setup = worksheet.page_setup
    
    page_setup.bottom_margin = 2.0
    page_setup.left_margin = 1.0
    page_setup.right_margin = 1.0
    page_setup.top_margin = 3.0
    
    workbook.save(str(data_dir / "SetMargins_out.xls"))
    # ExEnd:1

def center_on_page():
    # ExStart:CenterOnPage
    data_dir = get_data_dir()
    
    # Ensure the output directory exists
    ensure_directory_exists(data_dir)
    
    workbook = Workbook()
    worksheets = workbook.worksheets
    worksheet = worksheets[0]
    page_setup = worksheet.page_setup
    
    page_setup.center_horizontally = True
    page_setup.center_vertically = True
    
    workbook.save(str(data_dir / "CenterOnPage_out.xls"))
    # ExEnd:CenterOnPage

def header_and_footer_margins():
    # ExStart:HeaderAndFooterMargins
    data_dir = get_data_dir()
    
    # Ensure the output directory exists
    ensure_directory_exists(data_dir)
    
    workbook = Workbook()
    worksheets = workbook.worksheets
    worksheet = worksheets[0]
    page_setup = worksheet.page_setup
    
    page_setup.header_margin = 2.0
    page_setup.footer_margin = 2.0
    
    workbook.save(str(data_dir / "HeaderAndFooterMargins_out.xls"))
    # ExEnd:HeaderAndFooterMargins

if __name__ == "__main__":
    run()
    center_on_page()
    header_and_footer_margins()