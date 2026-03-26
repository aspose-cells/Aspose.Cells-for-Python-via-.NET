import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "ConsolidationFunctions"

def run():
    data_dir = get_data_dir()
    
    # Create workbook from source excel file
    workbook = cells.Workbook(str(data_dir / "Book.xlsx"))
    
    # Access the first worksheet of the workbook
    worksheet = workbook.worksheets[0]
    
    # Access the first pivot table of the worksheet
    pivot_table = worksheet.pivot_tables[0]
    
    # Apply Average consolidation function to first data field
    pivot_table.data_fields[0].function = cells.ConsolidationFunction.AVERAGE
    
    # Apply DistinctCount consolidation function to second data field
    pivot_table.data_fields[1].function = cells.ConsolidationFunction.DISTINCT_COUNT
    
    # Calculate the data to make changes affect
    pivot_table.calculate_data()
    
    # Saving the Excel file
    workbook.save(str(data_dir / "output.xlsx"))

if __name__ == "__main__":
    run()