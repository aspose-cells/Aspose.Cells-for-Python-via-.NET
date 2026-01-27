import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_adding_link_to_url():
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Add a hyperlink to a URL at cell B4
    worksheet.hyperlinks.add("B4", 1, 1, "https://www.aspose.com")
    worksheet.hyperlinks[0].text_to_display = "Aspose - File Format APIs"

    output_file = os.path.join(get_output_directory(), "outputAddingLinkToURL.xlsx")
    workbook.save(output_file)

    print("AddingLinkToURL executed successfully.")

if __name__ == "__main__":
    run_adding_link_to_url()
