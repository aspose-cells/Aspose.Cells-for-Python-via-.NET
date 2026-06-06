import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "02_OutputDirectory")

def main():
    # Create empty workbook.
    wb = Workbook()

    # Write protect workbook with password.
    wb.settings.write_protection.password = "1234"

    # Specify author while write protecting workbook.
    wb.settings.write_protection.author = "SimonAspose"

    # Save the workbook in XLSX format.
    output_path = os.path.join(get_output_directory(), "outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx")
    wb.save(output_path)

    print("SpecifyAuthorWhileWriteProtectingWorkbook executed successfully.")

if __name__ == "__main__":
    main()