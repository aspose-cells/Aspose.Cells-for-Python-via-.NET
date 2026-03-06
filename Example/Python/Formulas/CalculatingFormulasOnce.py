import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formulas/CalculatingFormulasOnce"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Load the template workbook
    workbook = cells.Workbook(str(data_dir / "book1.xls"))

    # Print the time before formula calculation
    print(datetime.now())

    # Set the CreateCalcChain as false
    workbook.settings.formula_settings.enable_calculation_chain = False

    # Calculate the workbook formulas
    workbook.calculate_formula()

    # Print the time after formula calculation
    print(datetime.now())
    # ExEnd:1

if __name__ == "__main__":
    run()