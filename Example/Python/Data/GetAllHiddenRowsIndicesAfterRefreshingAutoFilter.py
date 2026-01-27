import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_get_all_hidden_rows_indices_after_refreshing_autofilter():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx")
    workbook = cells.Workbook(input_file)
    worksheet = workbook.worksheets[0]

    worksheet.auto_filter.add_filter(0, "Orange")
    row_indices = worksheet.auto_filter.refresh(True)

    print("Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.")
    print("--------------------------")

    for r in row_indices:
        cell = worksheet.cells.get(r, 0)
        print(f"{r}\t{cell.name}\t{cell.string_value}")

    print("GetAllHiddenRowsIndicesAfterRefreshingAutoFilter executed successfully.")

if __name__ == "__main__":
    run_get_all_hidden_rows_indices_after_refreshing_autofilter()