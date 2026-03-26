import os
from pathlib import Path
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples"


def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Instantiating a Workbook object
    workbook = cells.Workbook()

    # Obtaining the reference of the newly added worksheet
    sheet = workbook.worksheets[0]

    cells_obj = sheet.cells

    # Setting the value to the cells
    cell = cells_obj.get("A1")
    cell.put_value("Sport")
    cell = cells_obj.get("B1")
    cell.put_value("Quarter")
    cell = cells_obj.get("C1")
    cell.put_value("Sales")

    cell = cells_obj.get("A2")
    cell.put_value("Golf")
    cell = cells_obj.get("A3")
    cell.put_value("Golf")
    cell = cells_obj.get("A4")
    cell.put_value("Tennis")
    cell = cells_obj.get("A5")
    cell.put_value("Tennis")
    cell = cells_obj.get("A6")
    cell.put_value("Tennis")
    cell = cells_obj.get("A7")
    cell.put_value("Tennis")
    cell = cells_obj.get("A8")
    cell.put_value("Golf")

    cell = cells_obj.get("B2")
    cell.put_value("Qtr3")
    cell = cells_obj.get("B3")
    cell.put_value("Qtr4")
    cell = cells_obj.get("B4")
    cell.put_value("Qtr3")
    cell = cells_obj.get("B5")
    cell.put_value("Qtr4")
    cell = cells_obj.get("B6")
    cell.put_value("Qtr3")
    cell = cells_obj.get("B7")
    cell.put_value("Qtr4")
    cell = cells_obj.get("B8")
    cell.put_value("Qtr3")

    cell = cells_obj.get("C2")
    cell.put_value(1500)
    cell = cells_obj.get("C3")
    cell.put_value(2000)
    cell = cells_obj.get("C4")
    cell.put_value(600)
    cell = cells_obj.get("C5")
    cell.put_value(1500)
    cell = cells_obj.get("C6")
    cell.put_value(4070)
    cell = cells_obj.get("C7")
    cell.put_value(5000)
    cell = cells_obj.get("C8")
    cell.put_value(6430)

    pivot_tables = sheet.pivot_tables

    # Adding a PivotTable to the worksheet
    index = pivot_tables.add("=A1:C8", "E3", "PivotTable2")

    # Accessing the instance of the newly added PivotTable
    pivot_table = pivot_tables[index]

    # Unshowing grand totals for rows.
    pivot_table.row_grand = False

    # Dragging the first field to the row area.
    pivot_table.add_field_to_area(cells.pivot.PivotFieldType.ROW, 0)

    # Dragging the second field to the column area.
    pivot_table.add_field_to_area(cells.pivot.PivotFieldType.COLUMN, 1)

    # Dragging the third field to the data area.
    pivot_table.add_field_to_area(cells.pivot.PivotFieldType.DATA, 2)

    # Saving the Excel file
    output_path = os.path.join(str(data_dir), "pivotTable_test_out.xls")
    workbook.save(output_path)
    # ExEnd:1


if __name__ == "__main__":
    run()