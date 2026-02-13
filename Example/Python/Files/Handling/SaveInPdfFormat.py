import os
import clr
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color
from datetime import datetime

clr.AddReference('System.Web')
from System.Web import HttpResponse


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/SaveInPdfFormat"


def run():
    data_dir = str(get_data_dir())
    response = None  # type: HttpResponse

    workbook = cells.Workbook()
    if response is not None:
        output_path = os.path.join(data_dir, "output.pdf")
        pdf_options = cells.PdfSaveOptions()
        workbook.save(response, output_path,
                      cells.SaveOptions.ContentDisposition.ATTACHMENT,
                      pdf_options)
        response.end()


if __name__ == "__main__":
    run()