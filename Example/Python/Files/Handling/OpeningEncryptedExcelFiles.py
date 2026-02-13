import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color


def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Handling"
        / "OpeningEncryptedExcelFiles"
    )


def run():
    data_dir = get_data_dir()
    load_options = cells.LoadOptions()
    load_options.password = "1234"
    wb_encrypted = cells.Workbook(str(data_dir / "encryptedBook.xls"), load_options)
    print("Encrypted excel file opened successfully!")