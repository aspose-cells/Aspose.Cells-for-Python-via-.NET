import aspose.cells as cells
from datetime import datetime
from pathlib import Path
import os

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Load sample workbook
    wb = cells.Workbook(str(source_dir / "sampleGroupPivotFieldsInPivotTable.xlsx"))
    
    # Access the second worksheet
    ws = wb.worksheets[1]
    
    # Access the pivot table
    pt = ws.pivot_tables[0]
    
    # Specify the start and end date time
    dt_start = datetime(2008, 1, 1)  # 1-Jan-2018
    dt_end = datetime(2008, 9, 5)    # 5-Sep-2018
    
    # Specify the group type list, we want to group by months and quarters
    # In Python version, use integer constants directly
    # 0 = Months, 1 = Quarters (based on PivotGroupByType enum values)
    group_type_list = [0, 1]  # 0=Months, 1=Quarters
    
    # Apply the grouping on first pivot field
    pt.set_manual_group_field(0, dt_start, dt_end, group_type_list, 1)
    
    # Refresh and calculate pivot table
    pt.refresh_data_flag = True
    pt.refresh_data()
    pt.calculate_data()
    pt.refresh_data_flag = False
    
    # Save the output Excel file
    output_file = str(output_dir / "outputGroupPivotFieldsInPivotTable.xlsx")
    wb.save(output_file)

if __name__ == "__main__":
    run()