import os
from pathlib import Path
from aspose import cells as cells
from aspose.cells import PdfSaveOptions
from aspose.cells.pivot import PivotFieldType

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())

    wb = cells.Workbook(os.path.join(source_dir, "SamplePivotSort.xlsx"))

    sheet = wb.worksheets[0]
    pivot_tables = sheet.pivot_tables

    # First PivotTable
    index = pivot_tables.add("=Sheet1!A1:C10", "E3", "PivotTable2")
    pivot_table = pivot_tables[index]
    pivot_table.row_grand = False
    pivot_table.column_grand = False
    pivot_table.add_field_to_area(PivotFieldType.ROW, 1)
    row_field = pivot_table.row_fields[0]
    row_field.is_auto_sort = True
    row_field.is_ascend_sort = True
    pivot_table.add_field_to_area(PivotFieldType.COLUMN, 0)
    col_field = pivot_table.column_fields[0]
    col_field.number_format = "dd/mm/yyyy"
    col_field.is_auto_sort = True
    col_field.is_ascend_sort = True
    pivot_table.add_field_to_area(PivotFieldType.DATA, 2)
    pivot_table.refresh_data()
    pivot_table.calculate_data()

    # Second PivotTable - sorted on SeaFood row field
    index = pivot_tables.add("=Sheet1!A1:C10", "E10", "PivotTable2")
    pivot_table = pivot_tables[index]
    pivot_table.row_grand = False
    pivot_table.column_grand = False
    pivot_table.add_field_to_area(PivotFieldType.ROW, 1)
    row_field = pivot_table.row_fields[0]
    row_field.is_auto_sort = True
    row_field.is_ascend_sort = True
    pivot_table.add_field_to_area(PivotFieldType.COLUMN, 0)
    col_field = pivot_table.column_fields[0]
    col_field.number_format = "dd/mm/yyyy"
    col_field.is_auto_sort = True
    col_field.is_ascend_sort = True
    col_field.auto_sort_field = 0
    pivot_table.add_field_to_area(PivotFieldType.DATA, 2)
    pivot_table.refresh_data()
    pivot_table.calculate_data()

    # Third PivotTable - sorted on 28/07/2000 column field
    index = pivot_tables.add("=Sheet1!A1:C10", "E18", "PivotTable2")
    pivot_table = pivot_tables[index]
    pivot_table.row_grand = False
    pivot_table.column_grand = False
    pivot_table.add_field_to_area(PivotFieldType.ROW, 1)
    row_field = pivot_table.row_fields[0]
    row_field.is_auto_sort = True
    row_field.is_ascend_sort = True
    row_field.auto_sort_field = 0
    pivot_table.add_field_to_area(PivotFieldType.COLUMN, 0)
    col_field = pivot_table.column_fields[0]
    col_field.number_format = "dd/mm/yyyy"
    col_field.is_auto_sort = True
    col_field.is_ascend_sort = True
    pivot_table.add_field_to_area(PivotFieldType.DATA, 2)
    pivot_table.refresh_data()
    pivot_table.calculate_data()

    wb.save(os.path.join(output_dir, "out.xlsx"))
    options = PdfSaveOptions()
    options.one_page_per_sheet = True
    wb.save(os.path.join(output_dir, "out.pdf"), options)

if __name__ == "__main__":
    run()