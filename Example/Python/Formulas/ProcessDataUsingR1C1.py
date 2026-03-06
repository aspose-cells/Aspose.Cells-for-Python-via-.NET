import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formulas/ProcessDataUsingR1C1"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Instantiating a Workbook object
    workbook = Workbook(str(data_dir / "Book1.xls"))

    worksheet = workbook.worksheets[0]

    # Setting an R1C1 formula on the "A11" cell, 
    # Row and Column indeces are relative to destination index
    worksheet.cells.get("A11").r1c1_formula = "=SUM(R[-10]C[0]:R[-7]C[0])"

    # Saving the Excel file
    workbook.save(str(data_dir / "output.xls"))
    # ExEnd:1