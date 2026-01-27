import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_preserve_single_quote_prefix_of_cell_value_or_range():
    # Create workbook
    workbook = cells.Workbook()

    # Access first worksheet
    worksheet = workbook.worksheets[0]

    # Access cell A1
    cell = worksheet.cells.get("A1")

    # Put some text in cell, it does not have Single Quote at the beginning
    cell.put_value("Text")
    style = cell.get_style()
    print(f"Quote Prefix of Cell A1: {style.quote_prefix}")

    # Put some text in cell, it has Single Quote at the beginning
    cell.put_value("'Text")
    style = cell.get_style()
    print(f"Quote Prefix of Cell A1: {style.quote_prefix}")

    # Print information about StyleFlag.QuotePrefix property
    print()
    print("When StyleFlag.QuotePrefix is False, it means, do not update the value of Cell.Style.QuotePrefix.")
    print("Similarly, when StyleFlag.QuotePrefix is True, it means, update the value of Cell.Style.QuotePrefix.")
    print()

    # Create an empty style
    style = workbook.create_style()

    # Create style flag - set StyleFlag.QuotePrefix as false
    flag = cells.StyleFlag()
    flag.quote_prefix = False

    # Create a range consisting of single cell A1
    rng = worksheet.cells.create_range("A1")

    # Apply the style to the range
    rng.apply_style(style, flag)

    # Access the style of cell A1
    style = cell.get_style()
    print(f"Quote Prefix of Cell A1: {style.quote_prefix}")

    # Create an empty style
    style = workbook.create_style()

    # Create style flag - set StyleFlag.QuotePrefix as true
    flag = cells.StyleFlag()
    flag.quote_prefix = True

    # Apply the style to the range
    rng.apply_style(style, flag)

    # Access the style of cell A1
    style = cell.get_style()
    print(f"Quote Prefix of Cell A1: {style.quote_prefix}")

    print("PreserveSingleQuotePrefixOfCellValueOrRange executed successfully.")

if __name__ == "__main__":
    run_preserve_single_quote_prefix_of_cell_value_or_range()