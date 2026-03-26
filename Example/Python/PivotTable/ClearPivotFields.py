from aspose import pydrawing as drawing
import aspose.cells as cells
from pathlib import Path
import os

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "ClearPivotFields"

def main():
    data_dir = get_data_dir()
    
    # Load a template file
    workbook = cells.Workbook(str(data_dir / "Book1.xls"))
    
    # Get the first worksheet
    sheet = workbook.worksheets[0]
    
    # Get the pivot tables in the sheet
    pivot_tables = sheet.pivot_tables
    
    # Get the first PivotTable
    pivot_table = pivot_tables[0]
    
    # Clear all the data fields
    pivot_table.data_fields.clear()
    
    # Add new data field
    pivot_table.add_field_to_area(cells.pivot.PivotFieldType.DATA, "Betrag Netto FW")
    
    # Set the refresh data flag on
    pivot_table.refresh_data_flag = False
    
    # Refresh and calculate the pivot table data
    pivot_table.refresh_data()
    pivot_table.calculate_data()
    
    # Saving the Excel file
    workbook.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    main()