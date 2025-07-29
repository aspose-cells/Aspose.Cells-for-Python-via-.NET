import pandas as pd
from aspose.cells import Workbook

# Create a new Aspose.Cells Workbook
workbook = Workbook()
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the cells
cells = worksheet.cells
# Add header and data values to specific cells
cells.get("A1").value = "Name"
cells.get("B1").value = "Age"
cells.get("C1").value = "City"
cells.get("A2").value = "Alice"
cells.get("B2").value = 25
cells.get("C2").value = "New York"
cells.get("A3").value = "Bob"
cells.get("B3").value = 30
cells.get("C3").value = "San Francisco"
cells.get("A4").value = "Charlie"
cells.get("B4").value = 35
cells.get("C4").value = "Los Angeles"

rowCount = cells.max_data_row
columnCount = cells.max_data_column

# Read the header row (row 0) and store column names
columnDatas = []
for c in range(columnCount + 1):
    columnDatas.append(cells.get_cell(0, c).value)

# Create an empty pandas DataFrame with column names from Excel
result = pd.DataFrame(columns=columnDatas, dtype=object)

# Read each data row (from row 1 onward) and add to the DataFrame
for i in range(1, rowCount + 1):
    rowarray = [cells.get_cell(i, j).value for j in range(columnCount + 1)]
    result.loc[i - 1] = rowarray

print(result)