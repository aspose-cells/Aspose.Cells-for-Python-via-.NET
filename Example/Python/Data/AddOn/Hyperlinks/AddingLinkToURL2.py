import os
import aspose.cells as cells
from aspose.pydrawing import Color

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_adding_link_to_url2():
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    cell = worksheet.cells.get("A1")
    cell.put_value("Visit Aspose")

    style = cell.get_style()
    style.font.color = Color.blue
    style.font.underline = cells.FontUnderlineType.SINGLE
    cell.set_style(style)

    worksheet.hyperlinks.add("A1", 1, 1, "https://www.aspose.com")

    output_path = os.path.join(get_output_directory(), "outputAddingLinkToURL2.xlsx")
    workbook.save(output_path)

    print("AddingLinkToURL2 executed successfully.")

if __name__ == "__main__":
    run_adding_link_to_url2()
