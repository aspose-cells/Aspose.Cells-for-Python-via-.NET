import aspose.cells as cells

def run_get_address_cell_count_offset_entire_column_and_entire_row_of_the_range():
    # Create empty workbook.
    workbook = cells.Workbook()
    # Access first worksheet.
    worksheet = workbook.worksheets[0]

    # Create range A1:B3.
    print("Creating Range A1:B3\n")
    rng = worksheet.cells.create_range("A1:B3")

    # Print range address.
    print("Range Address: " + rng.address)

    # Formatting console output.
    print("----------------------")
    print("")

    # Create range A1.
    print("Creating Range A1\n")
    rng = worksheet.cells.create_range("A1")

    # Print range offset, entire column and entire row.
    print("Offset: " + rng.get_offset(2, 2).address)
    print("Entire Column: " + rng.entire_column.address)
    print("Entire Row: " + rng.entire_row.address)

    # Formatting console output.
    print("----------------------")
    print("")

    print("GetAddressCellCountOffsetEntireColumnAndEntireRowOfTheRange executed successfully.")

if __name__ == "__main__":
    run_get_address_cell_count_offset_entire_column_and_entire_row_of_the_range()