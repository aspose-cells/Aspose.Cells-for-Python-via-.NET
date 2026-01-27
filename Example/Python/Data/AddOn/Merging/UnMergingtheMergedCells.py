import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..","..", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..","..", "..", "Data", "02_OutputDirectory"))

def run_un_merging_the_merged_cells():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "sampleUnMergingtheMergedCells.xlsx")
    workbook = cells.Workbook(input_path)

    worksheet = workbook.worksheets[0]
    worksheet.cells.un_merge(5, 2, 2, 3)

    output_path = os.path.join(output_dir, "outputUnMergingtheMergedCells.xlsx")
    workbook.save(output_path)

    print("UnMergingtheMergedCells executed successfully.")

if __name__ == "__main__":
    run_un_merging_the_merged_cells()
