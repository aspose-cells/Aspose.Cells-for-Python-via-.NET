import os
from pathlib import Path
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/AddingPageBreaks"


def main():
    data_dir = get_data_dir()
    
    # Instantiating a Workbook object
    workbook = cells.Workbook()
    
    # Add a page break at cell Y30
    workbook.worksheets[0].horizontal_page_breaks.add("Y30")
    workbook.worksheets[0].vertical_page_breaks.add("Y30")
    
    # Ensure output directory exists
    os.makedirs(data_dir, exist_ok=True)
    
    # Save the Excel file
    output_path = os.path.join(data_dir, "AddingPageBreaks_out.xls")
    workbook.save(output_path)


if __name__ == "__main__":
    main()