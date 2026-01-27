import os
import aspose.cells as cells

def get_data_dir() -> str:
    return os.path.abspath(os.path.join(".", "Data", "03_DataDirectory"))

def run_date_data_validation():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]
    sheet_cells = worksheet.cells

    # Put instruction text into A1
    sheet_cells.get("A1").put_value(
        "Please enter Date b/w 1/1/1970 and 12/31/1999"
    )
    sheet_cells.set_row_height(0, 31.0)
    sheet_cells.set_column_width(0, 35.0)

    validations = worksheet.validations

    # Define the first cell area (A1)
    ca = cells.CellArea()
    ca.start_row = 0
    ca.end_row = 0
    ca.start_column = 0
    ca.end_column = 0

    # Add validation for the defined area
    validation_index = validations.add(ca)
    validation = validations[validation_index]

    validation.type = cells.ValidationType.DATE
    validation.operator = cells.OperatorType.BETWEEN
    validation.formula1 = "1/1/1970"
    validation.formula2 = "12/31/1999"
    validation.show_error = True
    validation.alert_style = cells.ValidationAlertType.STOP
    validation.error_title = "Date Error"
    validation.error_message = "Enter a Valid Date"
    validation.input_message = "Date Validation Type"
    validation.ignore_blank = True
    validation.show_input = True

    # Define a second cell area (B1) and associate it with the same validation
    cell_area = cells.CellArea()
    cell_area.start_row = 0
    cell_area.end_row = 0
    cell_area.start_column = 1
    cell_area.end_column = 1
    validation.add_area(cell_area)

    # Save the workbook
    output_path = os.path.join(data_dir, "output.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_date_data_validation()
