import os
import aspose.cells as cells

def get_data_dir():
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "Data", "Processing"))

def run_tracing_precedents():
    data_dir = get_data_dir()
    workbook_path = os.path.join(data_dir, "Book1.xlsx")
    if not os.path.isfile(workbook_path):
        print(f"File not found: {workbook_path}")
        return

    workbook = cells.Workbook(workbook_path)
    worksheet = workbook.worksheets[0]
    cell = worksheet.cells.get("B4")

    precedents = cell.get_precedents()
    if precedents and len(precedents) > 0:
        area = precedents[0]
        print(area.sheet_name)
        print(cells.CellsHelper.cell_index_to_name(area.start_row, area.start_column))
        print(cells.CellsHelper.cell_index_to_name(area.end_row, area.end_column))

if __name__ == "__main__":
    run_tracing_precedents()