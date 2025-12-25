import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_password_protect_or_unprotect_shared_workbook():
    output_dir = get_output_directory()

    # Create empty Excel file
    workbook = cells.Workbook()

    # Protect the shared workbook with password
    workbook.protect_shared_workbook("1234")

    # Uncomment the following line to unprotect the shared workbook
    # workbook.unprotect_shared_workbook("1234")

    # Save the output Excel file
    output_path = os.path.join(output_dir, "outputProtectSharedWorkbook.xlsx")
    workbook.save(output_path)

    print("PasswordProtectOrUnprotectSharedWorkbook executed successfully.\n")

if __name__ == "__main__":
    run_password_protect_or_unprotect_shared_workbook()