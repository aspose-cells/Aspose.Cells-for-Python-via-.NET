import os
from aspose.cells import Workbook, SaveFormat
from datetime import datetime

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def main():
    # Create empty workbook
    wb = Workbook()

    # Access first worksheet
    ws = wb.worksheets[0]

    # Put some integer values in cell A1 and A2
    ws.cells.get("A1").put_value(10)
    ws.cells.get("A2").put_value(30)

    # Access cell C1 and set its formula
    c1 = ws.cells.get("C1")
    c1.formula = "=Sum(A1,A2)"

    # Add cell C1 into cell watches by name
    ws.cell_watches.add(c1.name)

    # Access cell E1 and set its formula
    e1 = ws.cells.get("E1")
    e1.formula = "=A2*A1"

    # Add cell E1 into cell watches by its row and column indices
    ws.cell_watches.add(e1.row, e1.column)

    # Save workbook to output XLSX format
    output_path = os.path.join(get_output_directory(), "outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx")
    wb.save(output_path, SaveFormat.XLSX)

    print("AddCellsToMicrosoftExcelFormulaWatchWindow executed successfully.")

if __name__ == "__main__":
    main()