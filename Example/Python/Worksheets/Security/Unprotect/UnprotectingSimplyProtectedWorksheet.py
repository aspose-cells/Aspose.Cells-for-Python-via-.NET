import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Unprotect/UnprotectingSimplyProtectedWorksheet"

def run():
    data_dir = get_data_dir()
    workbook = Workbook(os.path.join(data_dir, "book1.xls"))
    worksheet = workbook.worksheets[0]
    worksheet.unprotect()
    workbook.save(os.path.join(data_dir, "output.xls"), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    run()