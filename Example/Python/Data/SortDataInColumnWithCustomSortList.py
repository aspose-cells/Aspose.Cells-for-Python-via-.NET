import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_sort_data_in_column_with_custom_sort_list():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleSortData_CustomSortList.xlsx")
    workbook = cells.Workbook(input_file)

    worksheet = workbook.worksheets[0]

    cell_area = cells.CellArea.create_cell_area("A1", "A40")

    custom_sort_list = ["USA,US", "Brazil,BR", "China,CN", "Russia,RU", "Canada,CA"]

    workbook.data_sorter.add_key(0, cells.SortOrder.ASCENDING, custom_sort_list)
    workbook.data_sorter.sort(worksheet.cells, cell_area)

    output_file = os.path.join(output_dir, "outputSortData_CustomSortList.xlsx")
    workbook.save(output_file)

    print("SortDataInColumnWithCustomSortList executed successfully.")

if __name__ == "__main__":
    run_sort_data_in_column_with_custom_sort_list()