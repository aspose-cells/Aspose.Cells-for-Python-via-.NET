import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_create_union_range():
    output_dir = get_output_directory()

    # Instantiating a Workbook object
    workbook = cells.Workbook()

    # Create union range
    union_range = workbook.worksheets.create_union_range("sheet1!A1:A10,sheet1!C1:C10", 0)

    # Put value "ABCD" in the range
    union_range.value = "ABCD"

    # Save the output workbook
    output_path = os.path.join(output_dir, "CreateUnionRange_out.xlsx")
    workbook.save(output_path)

    print("CreateUnionRange executed successfully.")

if __name__ == "__main__":
    run_create_union_range()