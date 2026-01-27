import os
import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_sort_data_in_column_with_background_color():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleBackGroundFile.xlsx")
    workbook = cells.Workbook(input_file)

    sorter = workbook.data_sorter
    sorter.add_key(1, cells.SortOnType.CELL_COLOR, cells.SortOrder.DESCENDING, Color.red)

    cell_area = cells.CellArea.create_cell_area("A2", "C6")
    sorter.sort(workbook.worksheets[0].cells, cell_area)

    output_file = os.path.join(output_dir, "outputsampleBackGroundFile.xlsx")
    workbook.save(output_file)

    print("SortDataInColumnWithBackgroundColor executed successfully.")

if __name__ == "__main__":
    run_sort_data_in_column_with_background_color()
