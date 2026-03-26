import os
import aspose.cells as cells


def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "PivotTableExamples", "SpecifyCompatibility")


def Run():
    data_dir = get_data_dir()

    wb = cells.Workbook(os.path.join(data_dir, "sample-pivot-table.xlsx"))

    data_sheet = wb.worksheets[0]
    data_cells = data_sheet.cells
    cell = data_cells.get("A3")
    cell.put_value("FooBar")

    long_str = "Very long text 1. very long text 2. very long text 3. very long text 4. very long text 5. very long text 6. very long text 7. very long text 8. very long text 9. very long text 10. very long text 11. very long text 12. very long text 13. very long text 14. very long text 15. very long text 16. very long text 17. very long text 18. very long text 19. very long text 20. End of text."
    cell = data_cells.get("B3")
    cell.put_value(long_str)

    print("Length of original data string: " + str(len(cell.string_value)))

    cell = data_cells.get("C3")
    cell.put_value("closed")

    cell = data_cells.get("D3")
    cell.put_value("2016/07/21")

    pivot_sheet = wb.worksheets[1]
    pivot_table = pivot_sheet.pivot_tables[0]

    pivot_table.is_excel_2003_compatible = True
    pivot_table.refresh_data()
    pivot_table.calculate_data()

    b5 = pivot_sheet.cells.get("B5")
    print("Length of cell B5 after setting IsExcel2003Compatible property to True: " + str(len(b5.string_value)))

    pivot_table.is_excel_2003_compatible = False
    pivot_table.refresh_data()
    pivot_table.calculate_data()

    b5 = pivot_sheet.cells.get("B5")
    print("Length of cell B5 after setting IsExcel2003Compatible property to False: " + str(len(b5.string_value)))

    pivot_sheet.cells.set_row_height(b5.row, 100.0)
    pivot_sheet.cells.set_column_width(b5.column, 65.0)
    st = b5.get_style()
    st.is_text_wrapped = True
    b5.set_style(st)

    output_path = os.path.join(data_dir, "SpecifyCompatibility_out.xlsx")
    wb.save(output_path)


if __name__ == "__main__":
    Run()