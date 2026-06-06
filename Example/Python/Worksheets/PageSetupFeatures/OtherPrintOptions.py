import os
from pathlib import Path
from aspose.cells import Workbook
from aspose.cells import PrintCommentsType, PrintErrorsType

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets" / "PageSetupFeatures" / "OtherPrintOptions"

def main():
    data_dir = get_data_dir()
    
    os.makedirs(data_dir, exist_ok=True)
    
    workbook = Workbook()
    
    page_setup = workbook.worksheets[0].page_setup
    
    page_setup.print_gridlines = True
    page_setup.print_headings = True
    page_setup.black_and_white = True
    page_setup.print_comments = PrintCommentsType.PRINT_IN_PLACE
    page_setup.print_draft = True
    page_setup.print_errors = PrintErrorsType.PRINT_ERRORS_NA
    
    output_path = os.path.join(data_dir, "OtherPrintOptions_out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    main()