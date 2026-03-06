import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color
from pathlib import Path


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formulas/ProcessDataUsingArrayFunction"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"


def process_data_using_array_function():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
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
    
    # Adding a value to B1
    worksheet.cells.get("B1").put_value(4)
    
    # Adding a value to "B2" cell
    worksheet.cells.get("B2").put_value(5)
    
    # Adding a value to "B3" cell
    worksheet.cells.get("B3").put_value(6)
    
    # Adding a value to C1
    worksheet.cells.get("C1").put_value(7)
    
    # Adding a value to "C2" cell
    worksheet.cells.get("C2").put_value(8)
    
    # Adding a value to "C3" cell
    worksheet.cells.get("C3").put_value(9)
    
    # Adding a LINEST formula to "A6" cell
    worksheet.cells.get("A6").set_array_formula("=LINEST(A1:A3,B1:C3,TRUE,TRUE)", 5, 3)
    
    # Calculating the results of formulas
    workbook.calculate_formula()
    
    # Get the calculated value of the cell
    value = str(worksheet.cells.get("A6").value)
    
    # Saving the Excel file
    output_path = os.path.join(data_dir, "output.xls")
    workbook.save(output_path)


if __name__ == "__main__":
    process_data_using_array_function()