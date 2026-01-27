import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_setting_complex_formula_of_range():
    workbook = cells.Workbook()
    worksheets = workbook.worksheets

    # Add a new Named Range with name "data"
    index = worksheets.names.add("data")
    data = worksheets.names[index]
    data.refers_to = "=Sheet1!$A$1:$A$10"

    # Add another Named Range with name "range"
    index = worksheets.names.add("range")
    range_name = worksheets.names[index]
    range_name.refers_to = "=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)"

    output_file = os.path.join(get_output_directory(), "outputSettingComplexFormulaOfRange.xlsx")
    workbook.save(output_file)

    print("SettingComplexFormulaOfRange executed successfully.")

if __name__ == "__main__":
    run_setting_complex_formula_of_range()