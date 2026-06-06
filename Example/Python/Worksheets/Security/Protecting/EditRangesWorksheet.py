import os
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "Worksheets/Security/Protecting/EditRangesWorksheet")


def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "02_OutputDirectory")


def main():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Instantiate a new Workbook
    book = cells.Workbook()
    
    # Get the first (default) worksheet
    sheet = book.worksheets[0]
    
    # Get the Allow Edit Ranges
    allow_ranges = sheet.allow_edit_ranges
    
    # Create the range
    idx = allow_ranges.add("r2", 1, 1, 3, 3)
    proteced_range = allow_ranges[idx]
    
    # Specify the password
    proteced_range.password = "123"
    
    # Protect the sheet
    sheet.protect(cells.ProtectionType.ALL)
    
    # Save the Excel file
    output_path = os.path.join(data_dir, "protectedrange.out.xls")
    book.save(output_path)


if __name__ == "__main__":
    main()