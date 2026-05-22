from aspose.cells import Workbook, FileFormatType
import os
from pathlib import Path
from datetime import datetime

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    # Print message about XLS format.
    print("Maximum Rows and Columns supported by XLS format.")

    # Create workbook in XLS format.
    wb = Workbook(FileFormatType.EXCEL_97_TO_2003)

    # Print the maximum rows and columns supported by XLS format.
    max_rows = wb.settings.max_row + 1
    max_cols = wb.settings.max_column + 1
    print(f"Maximum Rows: {max_rows}")
    print(f"Maximum Columns: {max_cols}")
    print()

    # Print message about XLSX format.
    print("Maximum Rows and Columns supported by XLSX format.")

    # Create workbook in XLSX format.
    wb = Workbook(FileFormatType.XLSX)

    # Print the maximum rows and columns supported by XLSX format.
    max_rows = wb.settings.max_row + 1
    max_cols = wb.settings.max_column + 1
    print(f"Maximum Rows: {max_rows}")
    print(f"Maximum Columns: {max_cols}")

    print("FindMaximumRowsAndColumnsSupportedByXLSAndXLSXFormats executed successfully.")

if __name__ == "__main__":
    main()