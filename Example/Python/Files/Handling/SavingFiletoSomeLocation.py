import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/SavingFiletoSomeLocation"


def run():
    # The path to the documents directory.
    data_dir = get_data_dir()

    file_path = data_dir / "Book1.xls"

    # Load your source workbook
    workbook = cells.Workbook(str(file_path))

    # Save in Excel 97-2003 format
    workbook.save(str(data_dir) + ".output.xls")
    # OR
    workbook.save(str(data_dir) + ".output..xls", cells.SaveFormat.EXCEL_97_TO_2003)

    # Save in Excel2007 xlsx format
    workbook.save(str(data_dir) + ".output.xlsx", cells.SaveFormat.XLSX)

    # Save in Excel2007 xlsb format
    workbook.save(str(data_dir) + ".output.xlsb", cells.SaveFormat.XLSB)

    # Save in ods format
    workbook.save(str(data_dir) + ".output.ods", cells.SaveFormat.ODS)

    # Save in Pdf format
    workbook.save(str(data_dir) + ".output.pdf", cells.SaveFormat.PDF)

    # Save in Html format
    workbook.save(str(data_dir) + ".output.html", cells.SaveFormat.HTML)

    # Save in SpreadsheetML format
    workbook.save(str(data_dir) + ".output.xml", cells.SaveFormat.SPREADSHEET_ML)


if __name__ == "__main__":
    run()