import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory")
    )

def run_input_data_in_cells_in_range():
    # Instantiate a new Workbook.
    workbook = cells.Workbook()

    # Get the first worksheet.
    worksheet = workbook.worksheets[0]

    # Create a range based on H1:J4 and name it.
    cell_range = worksheet.cells.create_range("H1", "J4")
    cell_range.name = "MyRange"

    # Data to input.
    data = [
        ["USA", "Israel", "Iran"],
        ["UK", "AUS", "Canada"],
        ["Pakistan", "India", "Egypt"],
        ["China", "Philipine", "Brazil"]
    ]

    # Starting indices of the range.
    start_row = cell_range.first_row
    start_col = cell_range.first_column

    # Fill the cells within the range.
    for i, row_vals in enumerate(data):
        for j, val in enumerate(row_vals):
            worksheet.cells.get(start_row + i, start_col + j).put_value(val)

    # Ensure output directory exists.
    output_dir = get_output_directory()
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)

    # Save the workbook.
    output_path = os.path.join(output_dir, "outputInputDataInCellsInRange.xlsx")
    workbook.save(output_path)

    print("InputDataInCellsInRange executed successfully.")

if __name__ == "__main__":
    run_input_data_in_cells_in_range()
