import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def run():
    wb = Workbook()
    
    # Set the max rows of shared formula to 5
    wb.settings.max_rows_of_shared_formula = 5
    
    # Access first worksheet
    ws = wb.worksheets[0]
    
    # Access cell D1
    cell = ws.cells.get("D1")
    
    # Set the shared formula in 100 rows
    cell.set_shared_formula("=Sum(A1:A2)", 100, 1)
    
    # Save the output Excel file
    output_path = os.path.join(get_output_directory(), "outputSpecifyMaximumRowsOfSharedFormula.xlsx")
    wb.save(output_path)
    
    print("SpecifyMaximumRowsOfSharedFormula executed successfully.")

if __name__ == "__main__":
    run()