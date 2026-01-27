import os
import aspose.cells as cells

def get_data_directory():
    # Adjust the path as needed for your environment
    return os.path.abspath(os.path.join(".", "Data"))

def run_whole_number_data_validation():
    data_dir = get_data_directory()

    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]
    validations = worksheet.validations

    # Create CellArea for the initial validation cell (A1)
    ca = cells.CellArea()
    ca.start_row = 0
    ca.end_row = 0
    ca.start_column = 0
    ca.end_column = 0

    # Add validation and retrieve it
    validation = validations[validations.add(ca)]

    # Set validation type to whole number and operator to between
    validation.type = cells.ValidationType.WHOLE_NUMBER
    validation.operator = cells.OperatorType.BETWEEN

    # Set minimum and maximum values
    validation.formula1 = "10"
    validation.formula2 = "1000"

    # Define the range A1:B2
    area = cells.CellArea()
    area.start_row = 0
    area.end_row = 1
    area.start_column = 0
    area.end_column = 1

    # Apply the validation to the defined range
    validation.add_area(area)

    # Save the workbook
    output_path = os.path.join(data_dir, "output.out.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    run_whole_number_data_validation()