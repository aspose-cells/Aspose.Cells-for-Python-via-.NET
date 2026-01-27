import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_setting_simple_formula_with_range():
    output_dir = get_output_directory()

    # Create an instance of Workbook
    workbook = cells.Workbook()

    # Get the WorksheetCollection
    worksheets = workbook.worksheets

    # Add a new Named Range with name "NewNamedRange"
    index = worksheets.names.add("NewNamedRange")

    # Access the newly created Named Range
    name = worksheets.names[index]

    # Set RefersTo property of the Named Range to a formula
    name.refers_to = "=Sheet1!$A$3"

    # Set the formula in the cell A1 to the newly created Named Range
    worksheets[0].cells.get("A1").formula = "NewNamedRange"

    # Insert the value in cell A3 which is being referenced in the Named Range
    worksheets[0].cells.get("A3").put_value("This is the value of A3")

    # Calculate formulas
    workbook.calculate_formula()

    # Save the result in XLSX format
    output_path = os.path.join(output_dir, "outputSettingSimpleFormulaWithRange.xlsx")
    workbook.save(output_path)

    print("SettingSimpleFormulaWithRange executed successfully.")

if __name__ == "__main__":
    run_setting_simple_formula_with_range()
