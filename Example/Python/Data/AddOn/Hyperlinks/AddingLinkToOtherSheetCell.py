import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_adding_link_to_other_sheet_cell():
    workbook = cells.Workbook()
    workbook.worksheets.add()
    worksheet = workbook.worksheets[0]
    worksheet.hyperlinks.add("B3", 1, 1, "Sheet2!B9")
    worksheet.hyperlinks[0].text_to_display = "Link To Other Sheet Cell"
    output_path = os.path.join(get_output_directory(), "outputAddingLinkToOtherSheetCell.xlsx")
    workbook.save(output_path)
    print("AddingLinkToOtherSheetCell executed successfully.")

if __name__ == "__main__":
    run_adding_link_to_other_sheet_cell()