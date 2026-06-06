import os
from aspose.cells import Workbook, CopyOptions, PaperSizeType
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "Worksheets", "PageSetupFeatures", "CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet")

def copy_page_setup_settings_from_source_worksheet_to_destination_worksheet():
    # Create workbook
    wb = Workbook()

    # Add two test worksheets
    wb.worksheets.add("TestSheet1")
    wb.worksheets.add("TestSheet2")

    # Access both worksheets by name
    test_sheet1 = wb.worksheets.get("TestSheet1")
    test_sheet2 = wb.worksheets.get("TestSheet2")

    # Set the Paper Size of TestSheet1 to PaperA3ExtraTransverse
    test_sheet1.page_setup.paper_size = PaperSizeType.PAPER_A3_EXTRA_TRANSVERSE

    # Print the Paper Size of both worksheets
    print("Before Paper Size: " + str(test_sheet1.page_setup.paper_size))
    print("Before Paper Size: " + str(test_sheet2.page_setup.paper_size))
    print()

    # Copy the PageSetup from TestSheet1 to TestSheet2
    test_sheet2.page_setup.copy(test_sheet1.page_setup, CopyOptions())

    # Print the Paper Size of both worksheets
    print("After Paper Size: " + str(test_sheet1.page_setup.paper_size))
    print("After Paper Size: " + str(test_sheet2.page_setup.paper_size))
    print()

    print("CopyPageSetupSettingsFromSourceWorksheetToDestinationWorksheet executed successfully.\r\n")

if __name__ == "__main__":
    copy_page_setup_settings_from_source_worksheet_to_destination_worksheet()