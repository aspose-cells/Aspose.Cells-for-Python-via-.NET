import os
import decimal
import aspose.cells as cells

def get_data_directory():
    return os.path.abspath(os.path.join(".", "Data"))

def run_decimal_data_validation():
    data_dir = get_data_directory()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]
    validations = worksheet.validations

    # Create initial cell area for the validation (A1)
    init_area = cells.CellArea()
    init_area.start_row = 0
    init_area.end_row = 0
    init_area.start_column = 0
    init_area.end_column = 0

    validation_index = validations.add(init_area)
    validation = validations[validation_index]

    validation.type = cells.ValidationType.DECIMAL
    validation.operator = cells.OperatorType.BETWEEN

    validation.formula1 = str(-decimal.Decimal('79228162514264337593543950335'))
    validation.formula2 = str(decimal.Decimal('79228162514264337593543950335'))
    validation.error_message = "Please enter a valid integer or decimal number"

    # Specify the validation area (A1:A10)
    area = cells.CellArea()
    area.start_row = 0
    area.end_row = 9
    area.start_column = 0
    area.end_column = 0
    validation.add_area(area)

    output_path = os.path.join(data_dir, "output.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_decimal_data_validation()
