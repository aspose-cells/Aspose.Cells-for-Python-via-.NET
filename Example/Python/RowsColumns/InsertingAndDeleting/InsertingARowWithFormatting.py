import os
from datetime import datetime
from pathlib import Path
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/InsertingARowWithFormatting"


def main():
    data_dir = get_data_dir()
    
    # Creating a file stream containing the Excel file to be opened
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    # Instantiating a Workbook object
    # Opening the Excel file through the file stream
    workbook = cells.Workbook(fstream)
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Setting Formatting options
    insert_options = cells.InsertOptions()
    insert_options.copy_format_type = cells.CopyFormatType.SAME_AS_ABOVE
    
    # Inserting a row into the worksheet at 3rd position
    worksheet.cells.insert_rows(2, 1, insert_options)
    
    # Saving the modified Excel file
    output_path = os.path.join(data_dir, "InsertingARowWithFormatting.out.xls")
    workbook.save(output_path)
    
    # Closing the file stream to free all resources
    fstream.close()


if __name__ == "__main__":
    main()