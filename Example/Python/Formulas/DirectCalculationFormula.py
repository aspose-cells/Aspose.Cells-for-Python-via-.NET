import os
import sys
from datetime import datetime
from pathlib import Path
from aspose import pydrawing as drawing
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formulas/DirectCalculationFormula"

def run():
    data_dir = get_data_dir()

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    cell_a1 = worksheet.cells.get("A1")
    cell_a1.put_value(20)

    cell_a2 = worksheet.cells.get("A2")
    cell_a2.put_value(30)

    results = worksheet.calculate_formula("=Sum(A1:A2)")

    print("Value of A1: " + str(cell_a1.string_value))
    print("Value of A2: " + str(cell_a2.string_value))
    print("Result of Sum(A1:A2): " + str(results))

if __name__ == "__main__":
    run()