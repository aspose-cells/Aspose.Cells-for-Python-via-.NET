import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_detect_link_types():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "LinkTypes.xlsx")
    workbook = cells.Workbook(workbook_path)

    worksheet = workbook.worksheets[0]

    # Create a range A1:A7
    cell_range = worksheet.cells.create_range("A1", "A7")

    # Get hyperlinks in range
    hyperlinks = cell_range.hyperlinks

    for link in hyperlinks:
        print(f"{link.text_to_display}: {link.link_type}")

    print("DetectLinkTypes executed successfully.")

if __name__ == "__main__":
    run_detect_link_types()