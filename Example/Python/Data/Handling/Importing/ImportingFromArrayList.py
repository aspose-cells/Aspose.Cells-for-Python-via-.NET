import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_importing_from_arraylist():
    data_dir = get_output_directory()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    data_list = [
        "laurence chen",
        "roman korchagin",
        "kyle huang",
        "tommy wang"
    ]

    worksheet.cells.import_array_list(data_list, 0, 0, True)

    output_path = os.path.join(data_dir, "DataImport.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_importing_from_arraylist()