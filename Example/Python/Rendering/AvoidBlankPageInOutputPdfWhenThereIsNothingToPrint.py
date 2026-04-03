import os
import sys
from pathlib import Path
from datetime import datetime
from io import BytesIO

import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Rendering/AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint"

def main():
    # Create empty workbook.
    wb = cells.Workbook()

    # Create Pdf save options.
    opts = cells.PdfSaveOptions()

    # Default value of OutputBlankPageWhenNothingToPrint is true.
    # Setting false means - Do not output blank page when there is nothing to print.
    opts.output_blank_page_when_nothing_to_print = False

    # Save workbook to Pdf format, it will throw exception because workbook has nothing to print.
    ms = BytesIO()

    try:
        # Save to Pdf format. It will throw exception.
        wb.save(ms, opts)
    except Exception as ex:
        print("Exception Message: " + str(ex) + "\r\n")

    print("AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint executed successfully.")

if __name__ == "__main__":
    main()