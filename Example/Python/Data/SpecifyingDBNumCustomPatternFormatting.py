import os
import aspose.cells as cells

def get_data_dir():
    return os.path.abspath(os.path.join(".", "..","..",  "Data", "03_DataDirectory"))

def run_specifying_dbnum_custom_pattern_formatting():
    data_dir = get_data_dir()

    # Create a workbook.
    workbook = cells.Workbook()

    # Access first worksheet.
    worksheet = workbook.worksheets[0]

    # Access cell A1 and put value 123.
    cell = worksheet.cells.get("A1")
    cell.put_value(123)

    # Access cell style.
    style = cell.get_style()

    # Specifying DBNum custom pattern formatting.
    style.custom = "[DBNum2][$-804]General"

    # Set the cell style.
    cell.set_style(style)

    # Set the first column width.
    worksheet.cells.set_column_width(0, 30.0)

    # Save the workbook in output PDF format.
    output_file = os.path.join(data_dir, "outputDBNumCustomFormatting.pdf")
    workbook.save(output_file, cells.SaveFormat.PDF)

if __name__ == "__main__":
    run_specifying_dbnum_custom_pattern_formatting()
