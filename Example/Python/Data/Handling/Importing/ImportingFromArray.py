import os
import aspose.cells as cells

def get_data_dir():
    return os.path.abspath(os.path.join(".", "Data"))

def run_importing_from_array():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    names = ["laurence chen", "roman korchagin", "kyle huang"]
    worksheet.cells.import_array(names, 0, 0, True)

    output_path = os.path.join(data_dir, "DataImport.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_importing_from_array()