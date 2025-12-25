import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_extract_embedded_mol_file():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)

    workbook = cells.Workbook(os.path.join(source_dir, "EmbeddedMolSample.xlsx"))
    index = 1

    for sheet in workbook.worksheets:
        for ole in sheet.ole_objects:
            file_path = os.path.join(output_dir, f"OleObject{index}.mol")
            with open(file_path, "wb") as f:
                f.write(ole.object_data)
            index += 1

    print("ExtractEmbeddedMolFile executed successfully.")

if __name__ == "__main__":
    run_extract_embedded_mol_file()