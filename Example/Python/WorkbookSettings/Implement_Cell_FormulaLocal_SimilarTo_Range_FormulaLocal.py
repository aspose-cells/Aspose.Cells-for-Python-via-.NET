import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "WorkbookSettings/Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal"

# Custom globalization settings class
class CustomGlobalizationSettings:
    def get_local_function_name(self, standard_name):
        if standard_name == "SUM":
            return "UserFormulaLocal_SUM"
        if standard_name == "AVERAGE":
            return "UserFormulaLocal_AVERAGE"
        return ""

def run():
    # Create workbook
    wb = cells.Workbook()
    
    # Replace the internal globalization settings with custom implementation
    custom_gs = CustomGlobalizationSettings()
    
    # Access the worksheet and cell
    ws = wb.worksheets[0]
    cell = ws.cells.get("C4")
    
    # Assign SUM formula and print its FormulaLocal
    cell.formula = "SUM(A1:A2)"
    print("Formula Local: " + cell.formula_local)
    
    # Assign AVERAGE formula and print its FormulaLocal
    cell.formula = "=AVERAGE(B1:B2, B5)"
    print("Formula Local: " + cell.formula_local)
    
    print("Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal executed successfully.")

if __name__ == "__main__":
    run()