import os
import aspose.cells as cells

def get_data_dir():
    return os.path.abspath(os.path.join(".", "Data", "01_DataDirectory"))

def run_list_data_validation():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet1 = workbook.worksheets[0]

    # add second worksheet
    sheet_index = workbook.worksheets.add()
    worksheet2 = workbook.worksheets[sheet_index]

    # fill E1:E4 with color values
    colors = ["Blue", "Red", "Green", "Yellow"]
    for row_offset, color in enumerate(colors):
        cell = worksheet2.cells.get(row_offset, 4)   # column E = index 4
        cell.put_value(color)

    # create named range covering E1:E4
    rng = worksheet2.cells.create_range("E1", "E4")
    rng.name = "MyRange"

    # set up data validation on cell A1 of the first worksheet
    validations = worksheet1.validations
    ca = cells.CellArea()
    ca.start_row = 0
    ca.end_row = 0
    ca.start_column = 0
    ca.end_column = 0

    validation = validations[validations.add(ca)]
    validation.type = cells.ValidationType.LIST
    validation.operator = cells.OperatorType.NONE
    validation.in_cell_drop_down = True
    validation.formula1 = "=MyRange"
    validation.show_error = True
    validation.alert_style = cells.ValidationAlertType.STOP
    validation.error_title = "Error"
    validation.error_message = "Please select a color from the list"

    # expand validation area to A1:A5
    area = cells.CellArea()
    area.start_row = 0
    area.end_row = 4
    area.start_column = 0
    area.end_column = 0
    validation.add_area(area)

    output_path = os.path.join(data_dir, "output.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_list_data_validation()
