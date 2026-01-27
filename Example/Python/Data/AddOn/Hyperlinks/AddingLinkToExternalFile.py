import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_adding_link_to_external_file():
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    external_file_path = os.path.join(output_dir, "SomeExcelFile.xlsx")
    worksheet.hyperlinks.add("A5", 1, 1, external_file_path)
    worksheet.hyperlinks[0].text_to_display = "Link To External File"

    output_file = os.path.join(output_dir, "outputAddingLinkToExternalFile.xlsx")
    workbook.save(output_file)

    # Create the external file
    workbook = cells.Workbook()
    workbook.save(external_file_path)

    print("AddingLinkToExternalFile executed successfully.")

if __name__ == "__main__":
    run_adding_link_to_external_file()