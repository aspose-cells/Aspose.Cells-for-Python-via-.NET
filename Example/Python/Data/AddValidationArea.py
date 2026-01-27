import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_add_validation_area():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "ValidationsSample.xlsx")
    workbook = cells.Workbook(input_path)

    worksheet = workbook.worksheets[0]

    validation = worksheet.validations[0]

    cell_area = cells.CellArea.create_cell_area("D5", "E7")

    validation.add_area(cell_area, False, False)

    output_path = os.path.join(output_dir, "ValidationsSample_out.xlsx")
    workbook.save(output_path)

    print("AddValidationArea executed successfully.")

if __name__ == "__main__":
    run_add_validation_area()