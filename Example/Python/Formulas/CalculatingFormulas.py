import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formulas/CalculatingFormulas"

# Create directory if it is not already present.
data_dir = get_data_dir()
if not os.path.isdir(data_dir):
    os.makedirs(data_dir)

# Instantiating a Workbook object
workbook = Workbook()

# Adding a new worksheet to the Excel object
sheet_index = workbook.worksheets.add()

# Obtaining the reference of the newly added worksheet by passing its sheet index
worksheet = workbook.worksheets[sheet_index]

# Adding a value to "A1" cell
worksheet.cells.get("A1").put_value(1)

# Adding a value to "A2" cell
worksheet.cells.get("A2").put_value(2)

# Adding a value to "A3" cell
worksheet.cells.get("A3").put_value(3)

# Adding a SUM formula to "A4" cell
worksheet.cells.get("A4").formula = "=SUM(A1:A3)"

# Calculating the results of formulas
workbook.calculate_formula()

# Get the calculated value of the cell
value = str(worksheet.cells.get("A4").value)

# Saving the Excel file
workbook.save(os.path.join(data_dir, "output.xls"))