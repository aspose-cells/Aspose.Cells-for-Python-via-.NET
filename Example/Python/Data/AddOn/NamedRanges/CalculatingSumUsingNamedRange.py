import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_calculating_sum_using_named_range():
    workbook = cells.Workbook()
    worksheets = workbook.worksheets

    worksheets.get("Sheet1").cells.get("A1").put_value(10)

    first_new = worksheets.add()
    worksheets[first_new].cells.get("A1").put_value(10)

    range_index = worksheets.names.add("range")
    named_range = worksheets.names[range_index]
    named_range.refers_to = "=SUM(Sheet1!$A$1,Sheet2!$A$1)"

    second_new = worksheets.add()
    worksheets[second_new].cells.get("A1").formula = "range"

    workbook.calculate_formula()

    output_path = os.path.join(get_output_directory(), "outputCalculatingSumUsingNamedRange.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    run_calculating_sum_using_named_range()
