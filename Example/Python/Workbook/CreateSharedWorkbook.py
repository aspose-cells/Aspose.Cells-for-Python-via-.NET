import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_create_shared_workbook():
    output_dir = get_output_directory()
    workbook = cells.Workbook()
    workbook.settings.shared = True
    output_path = os.path.join(output_dir, "outputSharedWorkbook.xlsx")
    workbook.save(output_path)
    print("CreateSharedWorkbook executed successfully.\r\n")

if __name__ == "__main__":
    run_create_shared_workbook()