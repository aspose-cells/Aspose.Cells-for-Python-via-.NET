from datetime import datetime
import os
from aspose.cells import Workbook, PdfSaveOptions
from aspose.pydrawing import Color

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the Sample Workbook that throws Error on Excel2Pdf conversion
    wb = Workbook(os.path.join(source_dir, "sampleErrorExcel2Pdf.xlsx"))

    # Specify Pdf Save Options - Ignore Error
    opts = PdfSaveOptions()
    opts.ignore_error = True

    # Save the Workbook in Pdf with Pdf Save Options
    wb.save(os.path.join(output_dir, "outputErrorExcel2Pdf.pdf"))

    print("IgnoreErrorsWhileRenderingExcelToPdf executed successfully.\r\n")

if __name__ == "__main__":
    run()