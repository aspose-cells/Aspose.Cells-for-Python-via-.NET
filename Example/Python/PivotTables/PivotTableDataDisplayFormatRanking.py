import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.cells.pivot import PivotFieldDataDisplayFormat
from aspose.pydrawing import Color

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def get_output_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "02_OutputDirectory")

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "PivotTables", "PivotTableDataDisplayFormatRanking")

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = Workbook(os.path.join(source_dir, "PivotTableSample.xlsx"))

    worksheet = workbook.worksheets[0]
    pivot_index = 0

    pivot_table = worksheet.pivot_tables[pivot_index]
    pivot_fields = pivot_table.data_fields

    pivot_field = pivot_fields[0]

    pivot_field.data_display_format = PivotFieldDataDisplayFormat.RANK_LARGEST_TO_SMALLEST

    pivot_table.calculate_data()
    
    workbook.save(os.path.join(output_dir, "PivotTableDataDisplayFormatRanking_out.xlsx"))

    print("PivotTableDataDisplayFormatRanking executed successfully.")

if __name__ == "__main__":
    run()